import google.generativeai as genai
api_key = "AQ.Ab8RN6JHUxRPp0Z7nX4u1KAq1_l_FFPPh70a8GBnNHAgmb7e4g"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.8-flash")
response = model.generate_content("Think step by step and tell me what is 2+2")
print("Response text:", response.text)
print("Candidates:", response.candidates)
