from io import TextIOWrapper
from json import JSONDecodeError
import json
import os
import re
import time
import datetime
from typing import List, Optional, TextIO

import trec_car.read_data as trec_car

from .question_bank_loader import ExamQuestion, QueryQuestionBank, emit_test_bank_entry, write_single_query_test_bank, writeTestBank

from .openai_interface import default_openai_client, query_gpt_batch_with_rate_limiting
from .gemini_interface import default_gemini_client, query_gemini_batch_with_rate_limiting
from .davinci_to_runs_with_text import *


def _escape_unquoted_inner_double_quotes(text: str) -> str:
    """Repair bare double quotes inside JSON strings emitted by an LLM.

    A quote is treated as a real JSON string delimiter only when the next
    non-whitespace character is a JSON separator (or the end of the input).
    For example, this turns ``the "80/20 rule" in context`` into valid JSON
    without changing already-valid escaped quotes.
    """
    repaired = []
    in_string = False
    escaped = False

    for index, char in enumerate(text):
        if not in_string:
            repaired.append(char)
            if char == '"':
                in_string = True
            continue

        if escaped:
            repaired.append(char)
            escaped = False
            continue

        if char == "\\":
            repaired.append(char)
            escaped = True
            continue

        if char != '"':
            repaired.append(char)
            continue

        next_index = index + 1
        while next_index < len(text) and text[next_index].isspace():
            next_index += 1
        next_char = text[next_index] if next_index < len(text) else None

        if next_char is None or next_char in ",]}:":
            repaired.append(char)
            in_string = False
        else:
            repaired.append('\\"')

    return "".join(repaired)


def _loads_llm_json(text: str):
    """Parse strict JSON, with one conservative repair for common LLM output."""
    try:
        return json.loads(text)
    except JSONDecodeError as original_error:
        repaired = _escape_unquoted_inner_double_quotes(text)
        if repaired == text:
            raise original_error
        return json.loads(repaired)


def _parse_numbered_field_list(text: str, field_name: str) -> Optional[List[str]]:
    """Recover a numbered list placed inside a malformed JSON field.

    Some models emit ``{ "questions": [`` followed by ``1. question`` lines,
    without JSON quoting, commas, or even closing brackets.  Only accept this
    fallback when the requested field and opening array marker are present, so
    unrelated numbered prose is not silently treated as structured output.
    """
    field_match = re.search(
        rf'["\']?{re.escape(field_name)}["\']?\s*:\s*\[',
        text,
        flags=re.IGNORECASE,
    )
    if field_match is None:
        return None

    values = []
    expected_number = 1
    for line in text[field_match.end():].splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        item_match = re.match(r'^(\d+)[.)]\s+(.+?)\s*$', stripped)
        if item_match is None:
            if values:
                break
            continue

        number = int(item_match.group(1))
        if number != expected_number:
            return None

        value = item_match.group(2).strip().rstrip(",")
        if not value:
            return None
        values.append(value)
        expected_number += 1

    return values or None


class FetchGptJson:

    def __init__(self, gpt_model:str, max_tokens:int):
        self.gpt_model = gpt_model
        self.max_tokens = max_tokens


    def set_json_instruction(self, json_instruction:str, field_name:str):
        self._json_instruction = json_instruction
        self._field_name = field_name


    def generation_info(self, test_collection:str, hash:str, description:Optional[str]):
        return {"gpt_model":self.gpt_model
                , "format_instruction":"json"
                , "prompt_style": "Explore the connection..."
                , "prompt_target": self._field_name
                , "test_collection": test_collection
                , "hash":hash
                , "description":description
                }


    def __is_list_of_strings(self, lst):
        return isinstance(lst, list) and all(isinstance(item, str) for item in lst)

    # def _parse_json_response(self, gpt_response:str) -> Optional[List[str]]:
    #     cleaned_gpt_response=""
    #     if gpt_response.strip().startswith("{"):
    #         cleaned_gpt_response=gpt_response.strip()
    #     elif gpt_response.startswith("```json"):
    #         cleaned_gpt_response= re.sub(r'```json|```', '', gpt_response).strip()
    #     else:
    #         print(f"Not sure how to parse ChatGPT response from json:\n {gpt_response}")
    #         cleaned_gpt_response=gpt_response

    #     try:
    #         response = json.loads(cleaned_gpt_response)
    #         list = response.get(self._field_name)
    #         if(self.__is_list_of_strings(list)) is not None:
    #             return list
    #         else:
    #             return None
    #     except JSONDecodeError as e:
    #         print(e)
    #         return None

    def _parse_json_response(self, gpt_response: str) -> Optional[List[str]]:
        resp = gpt_response.strip()

        # First try parsing the whole response directly
        try:
            response = _loads_llm_json(resp)
        except JSONDecodeError:
            # Handle ```json ... ``` or ``` ... ```
            if resp.startswith("```"):
                cleaned = re.sub(r'^```(?:json)?\s*|\s*```$', '', resp,
                                 flags=re.IGNORECASE | re.DOTALL).strip()
                try:
                    response = _loads_llm_json(cleaned)
                except JSONDecodeError:
                    response = None
            else:
                response = None

            # Handle prose before/after a valid JSON object
            if response is None:
                start = resp.find("{")
                end = resp.rfind("}")

                if start != -1 and end != -1 and end > start:
                    cleaned = resp[start:end + 1]
                    try:
                        response = _loads_llm_json(cleaned)
                    except JSONDecodeError as e:
                        print(f"Could not parse extracted JSON: {e}")
                        print(f"Extracted text:\n{cleaned}")
                        return _parse_numbered_field_list(resp, self._field_name)
                else:
                    print(f"Could not find JSON object in response:\n{gpt_response}")
                    return _parse_numbered_field_list(resp, self._field_name)

        if response is None:
            return _parse_numbered_field_list(resp, self._field_name)

        values = response.get(self._field_name)

        if self.__is_list_of_strings(values):
            return values

        print(
            f"Expected '{self._field_name}' to be a list of strings, "
            f"but got: {values}"
        )
        return None

    def _generate(self, prompt:str, gpt_model:str,max_tokens:int,system_message:Optional[str]=None, **kwargs)->str:
        answer = query_gpt_batch_with_rate_limiting(prompt, use_chat_interface=True, client=default_openai_client(), gpt_model=gpt_model, max_tokens=max_tokens, system_message=system_message,temperature=0.0, **kwargs)
        return answer

    def generate_question(self, prompt:str, system_message:Optional[str]=None, **kwargs):
        full_prompt = prompt+self._json_instruction

        print("\n\n"+full_prompt+"\n\n")

        tries = 3
        while tries>0:
            response = self._generate( prompt=full_prompt
                                      , gpt_model=self.gpt_model
                                      , max_tokens=self.max_tokens
                                      , system_message=system_message
                                      , **kwargs)
            questions = self._parse_json_response(response)
            if questions is not None:
                return questions
            else:
                tries-=1
                print(f"Receiving unparsable response: {response}. Tries left: {tries}")
        return None

            

class FetchGptQuestions(FetchGptJson):
    def __init__(self, gpt_model:str, max_tokens:int):
        super().__init__(gpt_model=gpt_model, max_tokens=max_tokens)
        json_instruction= r'''
Give the question set in the following JSON format:
```json
{ "questions": [question_text_1, question_text_2, ... ] }
```'''
        field_name="questions"
        self.set_json_instruction(json_instruction=json_instruction, field_name=field_name)


class FetchGptNuggets(FetchGptJson):
    def __init__(self, gpt_model:str, max_tokens:int):
        super().__init__(gpt_model=gpt_model, max_tokens=max_tokens)
        json_instruction= r'''
Give the nugget set in the following JSON format:
```json
{ "nuggets": [nugget_text_1, nugget_text2, ... ] }
```'''
        field_name="nuggets"
        self.set_json_instruction(json_instruction=json_instruction, field_name=field_name)


class FetchGeminiJson(FetchGptJson):
    def __init__(self, gemini_model:str, max_tokens:int, think:bool=False):
        super().__init__(gpt_model=gemini_model, max_tokens=max_tokens)
        self.think = think

    def _generate(self, prompt:str, gpt_model:str,max_tokens:int,system_message:Optional[str]=None, **kwargs)->str:
        answer = query_gemini_batch_with_rate_limiting(prompt, use_chat_interface=True, client=default_gemini_client(), gemini_model=gpt_model, max_tokens=max_tokens, system_message=system_message, think=self.think, **kwargs)
        return answer

class FetchGeminiQuestions(FetchGeminiJson):
    def __init__(self, gemini_model:str, max_tokens:int, think:bool=False):
        super().__init__(gemini_model=gemini_model, max_tokens=max_tokens, think=think)
        json_instruction= r'''
Give the question set in the following JSON format:
```json
{ "questions": [question_text_1, question_text_2, ... ] }
```'''
        field_name="questions"
        self.set_json_instruction(json_instruction=json_instruction, field_name=field_name)


class FetchGeminiNuggets(FetchGeminiJson):
    def __init__(self, gemini_model:str, max_tokens:int, think:bool=False):
        super().__init__(gemini_model=gemini_model, max_tokens=max_tokens, think=think)
        json_instruction= r'''
Give the nugget set in the following JSON format:
```json
{ "nuggets": [nugget_text_1, nugget_text2, ... ] }
```'''
        field_name="nuggets"
        self.set_json_instruction(json_instruction=json_instruction, field_name=field_name)


# ---------------- CAR Y3 -------------------

def car_section_question_prompt(query_title:str, query_subtopic:str)->str:
    return f'''Explore the connection between '{query_title}' with a specific focus on the subtopic '{query_subtopic}'.
        Generate insightful questions that delve into advanced aspects of '{query_subtopic}', showcasing a deep understanding of the subject matter. Avoid basic or introductory-level inquiries. '''
    
def car_section_nugget_prompt(query_title:str, query_subtopic:str)->str:
    return f'''Explore the connection between '{query_title}' with a specific focus on the subtopic '{query_subtopic}'.
        Generate insightful nuggets (key facts) that delve into advanced aspects of '{query_subtopic}', showcasing a deep understanding of the subject matter. Avoid basic or introductory-level nuggets. Keep nuggets to a maximum of 4 words.'''    


def generate_questions_cary3(car_outlines_path:Path
                             , fetcher: FetchGptJson
                             , out_file:TextIO
                             , use_nuggets:bool
                             , test_collection:str="cary3"
                             , description:Optional[str]=None
                             , max_queries:Optional[int]=None, system_message:Optional[str]=None, **kwargs):
   
    hash=datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    generation_info = fetcher.generation_info(test_collection=test_collection, hash= hash, description=description)
    
    page:trec_car.Page
    for page in itertools.islice(trec_car.iter_outlines(open(car_outlines_path, 'rb')), max_queries):
        query_id = page.page_id
        title_query = page.page_name

        section:trec_car.Section
        for section in page.child_sections:
            query_facet_id = section.headingId
            section_query = section.heading
            query_text = f'{title_query} / {section_query}'

            print(query_id, query_facet_id, title_query, section_query)
            prompt =""
            if use_nuggets:
                prompt = car_section_nugget_prompt(query_title=title_query, query_subtopic=section_query)
            else:
                prompt = car_section_question_prompt(query_title=title_query, query_subtopic=section_query)


            questions = fetcher.generate_question(prompt, system_message=system_message, **kwargs)
            emit_test_bank_entry(out_file=out_file
                                 , test_collection=test_collection
                                 , generation_info= generation_info
                                 , query_id= query_id
                                 , query_facet_id= query_facet_id
                                 , query_facet_text=section_query
                                 , query_text= query_text
                                 , question_texts =questions
                                 , use_nuggets=use_nuggets)

#  ------------------- TREC DL ------------------



def web_search_question_prompt(query_text:str)->str:
    return f'''Break the query '{query_text}' into concise questions that must be answered. 
     Generate 10 concise insightful questions that reveal whether information relevant for '{query_text}' was provided, showcasing a deep understanding of the subject matter. Avoid basic or introductory-level inquiries. Keep the questions short.'''



def web_search_nugget_prompt(query_text:str)->str:
    return f'''Break the query '{query_text}' into concise nuggets that must be mentioned. 
     Generate 10 concise insightful nuggets that reveal whether information relevant for '{query_text}' was provided, showcasing a deep understanding of the subject matter. Avoid basic or introductory-level nuggets. Keep nuggets to a maximum of 4 words.'''


def generate_questions_json(query_json:Path
                            , fetcher: FetchGptJson
                            , out_file:TextIO
                            , test_collection:str
                            , use_nuggets:bool
                            , description:Optional[str]=None
                            , max_queries:Optional[int]=None
                            , system_message:Optional[str]=None, **kwargs):

    hash=datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    generation_info = fetcher.generation_info(test_collection=test_collection, hash= hash, description=description)
    
    queries:Dict[str,str]
    with open(query_json, "rt", encoding="utf-8") as file:
        queries = json.load(file)

        for query_id, query_text in itertools.islice(queries.items(), max_queries):
            print(query_id, query_text)
            if not use_nuggets:
                prompt = web_search_question_prompt(query_text=query_text)
            elif use_nuggets:
                prompt = web_search_nugget_prompt(query_text=query_text)

            questions = fetcher.generate_question(prompt, system_message=system_message, **kwargs)
            emit_test_bank_entry(out_file=out_file
                                 , test_collection=test_collection
                                 , generation_info= generation_info
                                 , query_id= query_id
                                 , query_facet_id= None
                                 , query_facet_text=None
                                 , query_text= query_text
                                 , question_texts =questions
                                 , use_nuggets=use_nuggets)

# -------------------------------------------
            

def noodle_car_gpt(car_outlines_cbor:Path, gpt_out:Path, gpt_model:str, use_nuggets:bool, model_api:str='openai', think:bool=False, max_tokens:int=1500, description:Optional[str]=None,max_queries:Optional[int]=None):
    fetcher:FetchGptJson
    if model_api == 'openai':
        if use_nuggets:
            fetcher = FetchGptNuggets(gpt_model=gpt_model, max_tokens=max_tokens)
        else:
            fetcher = FetchGptQuestions(gpt_model=gpt_model, max_tokens=max_tokens)
    elif model_api == 'gemini':
        if use_nuggets:
            fetcher = FetchGeminiNuggets(gemini_model=gpt_model, max_tokens=max_tokens, think=think)
        else:
            fetcher = FetchGeminiQuestions(gemini_model=gpt_model, max_tokens=max_tokens, think=think)


    with gzip.open(gpt_out, "wt", encoding='utf-8') as file:
        generate_questions_cary3(car_outlines_path = car_outlines_cbor, fetcher=fetcher, out_file = file, use_nuggets=use_nuggets, description=description, max_queries=max_queries)

        file.close()

def noodle_json_query_gpt(query_json:Path, gpt_out:Path, gpt_model:str, use_nuggets:bool, test_collection:str, model_api:str='openai', think:bool=False, description:Optional[str]=None, max_tokens:int=1500, max_queries:Optional[int]=None):
    fetcher:FetchGptJson
    if model_api == 'openai':
        if not use_nuggets:
            fetcher = FetchGptQuestions(gpt_model=gpt_model, max_tokens=max_tokens)
        elif use_nuggets:
            fetcher = FetchGptNuggets(gpt_model=gpt_model, max_tokens=max_tokens)
    elif model_api == 'gemini':
        if not use_nuggets:
            fetcher = FetchGeminiQuestions(gemini_model=gpt_model, max_tokens=max_tokens, think=think)
        elif use_nuggets:
            fetcher = FetchGeminiNuggets(gemini_model=gpt_model, max_tokens=max_tokens, think=think)


    with gzip.open(gpt_out, "wt", encoding='utf-8') as file:
        generate_questions_json(query_json = query_json, fetcher=fetcher, out_file = file, use_nuggets=use_nuggets, test_collection=test_collection, description=description, max_queries=max_queries)

        file.close()





def main():
    import argparse

    query_json_format=r'''
        {
          "query_id_1":"query text",
          "query_id_2":"query text",
          "query_id_3":"query text",
          ...
        }
'''
    desc = r'''Generate Questions for CAR Queries'''
    
    parser = argparse.ArgumentParser(description="Question Generation"
                                   , epilog=desc
                                   , formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-c','--car-outlines-cbor', type=str, metavar='CAR_OUTLINES_CBOR'
                        , help='Input TREC CAR ourlines file (from which page-level queries and order of sections/facets will be taken)'
                        )
    
    parser.add_argument('-q','--query-json', type=str, metavar='JSON'
                        , help=f'Input query-file in JSON format: {query_json_format}'
                        )
    
    parser.add_argument('--use-nuggets', action='store_true', help="if set uses nuggets instead of questions")


    parser.add_argument('-o', '--out-file', type=str, metavar='runs-xxx.jsonl.gz', required=True
                        , help='Output file name where paragraphs with exam grade annotations will be written to')

    parser.add_argument('--gpt-model', type=str, metavar='MODEL', default="gpt-3.5-turbo", help='OpenAI model name to be used')
    parser.add_argument('--model-api', type=str, choices=['openai', 'gemini'], default='openai', help='API backend to use (openai or gemini)')
    parser.add_argument('--think', action='store_true', help='Enable reasoning (thinking) for models that support it')
    parser.add_argument('--test-collection', type=str, required=True, metavar='NAME', help='Test collection where queries are taken from.')
    parser.add_argument('--max-tokens', type=int, metavar='NUM', default=1500, help='Max Tokens from API')
    parser.add_argument('--max-queries', type=int, metavar='INT', default=None, help='limit the number of queries that will be processed (for debugging)')
    parser.add_argument('--description', type=str, metavar='DESC', default=None, help='Description of the generated question set')

    args = parser.parse_args()  

    if not (args.car_outlines_cbor  or args.query_json):
        raise RuntimeError("Either --car-outines-cbor or --query-json must be set.")
    if  (args.car_outlines_cbor  and args.query_json):
        raise RuntimeError("Either --car-outines-cbor or --query-json must be set. (not both)")

    if args.car_outlines_cbor is not None:
        noodle_car_gpt(car_outlines_cbor=args.car_outlines_cbor, gpt_model=args.gpt_model, gpt_out=args.out_file, max_tokens=args.max_tokens, use_nuggets = args.use_nuggets, model_api=args.model_api, think=args.think, max_queries=args.max_queries, description=args.description)

    if args.query_json is not None:
        noodle_json_query_gpt(query_json=args.query_json, gpt_model=args.gpt_model, gpt_out=args.out_file, max_tokens=args.max_tokens, use_nuggets = args.use_nuggets, test_collection=args.test_collection, model_api=args.model_api, think=args.think, description=args.description , max_queries=args.max_queries)

if __name__ == "__main__":
    main()
