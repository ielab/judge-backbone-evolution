import os
from google import genai
from google.genai import types

api_key = "AQ.Ab8RN6JHUxRPp0Z7nX4u1KAq1_l_FFPPh70a8GBnNHAgmb7e4g"
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Think step by step and tell me what is 2+2',
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                include_thoughts=True,
                thinking_budget=256
            )
        )
    )
    print("Parts:")
    for i, part in enumerate(response.candidates[0].content.parts):
        print(f"Part {i}:")
        if hasattr(part, 'thought') and part.thought:
            print("THOUGHT:", part.text)
        elif getattr(part, 'thought', False) == True:
            print("THOUGHT:", part.text)
        elif part.text:
            print("TEXT:", part.text)
        else:
            print("OTHER:", part)
except Exception as e:
    print(f"Error: {e}")
