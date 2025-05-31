import time
from openai import OpenAI
from google import genai
from google.genai import types
from dotenv import load_dotenv


class ResponseGenerator:
    
    def __init__(self):
        load_dotenv()
        self.openai_client = OpenAI()
        self.gemini_client = genai.Client()

    def generate_openai_response(self, system_prompt, user_prompt):
        response = self.openai_client.responses.create(
            model="gpt-4o-mini",
            instructions=system_prompt,
            input=user_prompt
        )
        return response.output_text
    
    def generate_gemini_response(self, system_prompt, user_prompt):
        delay = 2
        while True:
            try:
                response = self.gemini_client.models.generate_content(
                    model="gemini-2.0-flash-001",
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                    ),
                )
                return response.text
            except Exception as e:
                time.sleep(delay)
                print("Retry")
                delay *= 2