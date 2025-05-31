from openai import OpenAI
from dotenv import load_dotenv


class ResponseGenerator:
    
    def __init__(self):
        load_dotenv()
        self.openai_client = OpenAI()

    def generate_response(self, system_prompt, user_prompt):
        response = self.openai_client.responses.create(
            model="gpt-4o-mini",
            instructions=system_prompt,
            input=user_prompt
        )
        return response.output_text