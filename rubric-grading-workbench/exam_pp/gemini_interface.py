import datetime
import json
from json import JSONDecodeError
import os
import random
import re
from typing import Optional, Union, List
import time

from .exam_llm import LlmResponseError
from .openai_interface import OpenAIRateLimiter, global_rate_limiter, retry_with_exponential_backoff

from google import genai
from google.genai import types
from google.genai.errors import APIError

def createGeminiClient(api_key:Optional[str]=os.getenv('GEMINI_API_KEY')):
    if api_key is None:
        raise RuntimeError("api_key must either be set as argument or via environment variable \"GEMINI_API_KEY\"")
    return genai.Client(api_key=api_key)

_client:Optional[genai.Client] = None

def default_gemini_client() -> genai.Client:
    global _client
    if _client is None:
        _client = createGeminiClient()
    return _client

def query_gemini_batch_with_rate_limiting(prompt:str, gemini_model:str, max_tokens:int, use_chat_interface:bool, client=None, rate_limiter:Optional[OpenAIRateLimiter]=None, system_message:Optional[str]=None, think:bool=False, **kwargs):
    if client is None:
        client = default_gemini_client()
    if rate_limiter is None:
        rate_limiter = global_rate_limiter

    rate_limiter.wait_if_needed()

    config_args = {
        "max_output_tokens": max_tokens,
    }
    if system_message is not None:
        config_args["system_instruction"] = system_message

    if think:
        #    if think:
        config_args["thinking_config"] = {"thinking_budget": 1024}

    # Pass remaining kwargs to config if any, filtering unsupported ones
    # (Just a safety fallback)
    config = types.GenerateContentConfig(**config_args)

    def do_generate():
        return client.models.generate_content(
            model=gemini_model,
            contents=prompt,
            config=config,
        )

    # Note: we use APIError which is the google-genai base error class
    completion = retry_with_exponential_backoff(func=do_generate, errors=(APIError,))()
    
    if not completion or not hasattr(completion, "text") or completion.text is None:
        raise ValueError(f"Invalid completion response: {completion}")

    result_text = completion.text.strip()

    # Update rate limits (heuristic since genai usage might not map 1:1, but we approximate)
    used_tokens = 0
    if hasattr(completion, 'usage_metadata') and completion.usage_metadata is not None:
        used_tokens = completion.usage_metadata.total_token_count
    else:
        # Approximate if usage is missing
        used_tokens = len(prompt.split()) + len(result_text.split())

    rate_limiter.update_limits(used_tokens)

    return result_text


class FetchGeminiJson:
    def __init__(self, gemini_model:str, max_tokens:int, client=None, use_chat_protocol:bool=True, think:bool=False):
        self.client = client if client is not None else default_gemini_client()
        self.gemini_model = gemini_model
        self.max_tokens = max_tokens
        self.use_chat_protocol = use_chat_protocol
        self.think = think


    def set_json_instruction(self, json_instruction:str, field_name:str):
        self._json_instruction = json_instruction
        self._field_name = field_name


    def generation_info(self):
        return {"gemini_model":self.gemini_model
                , "format_instruction":"json"
                , "prompt_target": self._field_name
                , "think": self.think
                }


    def __is_list_of_strings(self, lst):
        return isinstance(lst, list) and all(isinstance(item, str) for item in lst)

    def __is_int(self, i):
        return isinstance(i,int)

    def _parse_json_response(self, gemini_response:str, request:Optional[str]=None) -> Optional[str]:
        resp = gemini_response.strip()
        cleaned_gemini_response=""
        if resp.startswith("{"):
            cleaned_gemini_response=resp
        elif resp.startswith("```json"):
            cleaned_gemini_response= re.sub(r'```json|```', '', resp).strip()
        elif resp.startswith("```"):
            cleaned_gemini_response= re.sub(r'```|```', '', resp).strip()
        else:
            print(f"Not sure how to parse Gemini response from json:\n-----\n{request}\n-----\n{gemini_response}\n----")
            cleaned_gemini_response=resp

        try:
            response = json.loads(cleaned_gemini_response)
            grade = response.get(self._field_name)
            if(self.__is_int(grade)) is not None:
                return f"{grade}"
            else:
                return None
        except JSONDecodeError as e:
            print(e)
            return None

    def _generate(self, prompt:str, gemini_model:str,max_tokens:int, rate_limiter:OpenAIRateLimiter, system_message:Optional[str]=None, **kwargs)->str:
        answer = query_gemini_batch_with_rate_limiting( prompt, gemini_model=gemini_model, max_tokens=max_tokens, client=self.client, rate_limiter=rate_limiter, use_chat_interface=self.use_chat_protocol, system_message=system_message, think=self.think, **kwargs)
        return answer

    async def generate_request(self, prompt:str, rate_limiter:OpenAIRateLimiter, system_message:Optional[str]=None, **kwargs)->Union[str, LlmResponseError]:
        full_prompt = prompt+self._json_instruction

        tries = 3
        while tries>0:
            try:
                import asyncio
                response = await asyncio.to_thread(
                                        self._generate,
                                        prompt=full_prompt,
                                        gemini_model=self.gemini_model,
                                        max_tokens=self.max_tokens,
                                        rate_limiter=rate_limiter,
                                        system_message=system_message,
                                        **kwargs
                                        )
                
                reqs = self._parse_json_response(response, request=full_prompt)
                if reqs is not None:
                    return reqs
                else:
                    tries-=1
                    print(f"Receiving unparsable response: {response}. Tries left: {tries}")
            except APIError as ex:
                return LlmResponseError(failure_reason="Exception from Llm:", response="",prompt=prompt, caught_exception=str(ex))
        return LlmResponseError(failure_reason="Could not parse LLM response after 3 tries.", response=response, prompt=prompt, caught_exception=None)
