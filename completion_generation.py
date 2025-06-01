from prompts import RESPONSE_SYSTEM_PROMPT, RESPONSE_USER_PROMPT
from response_generator import ResponseGenerator
import pandas as pd

DATASET_PATH = "dataset.csv"
PRINT_INTERVAL = 10


if __name__ == "__main__":
    LLM = ResponseGenerator()
    dataset = pd.read_csv(DATASET_PATH)
    total = len(dataset)
    dataset['response'] = ""
    for idx, record in dataset.iterrows():
        user_prompt = RESPONSE_USER_PROMPT.format(input=record['prompt'], emotional_description=record['emotional_description'])
        response = LLM.generate_gemini_response(RESPONSE_SYSTEM_PROMPT, user_prompt)
        dataset.at[idx, 'response'] = response
        if (idx + 1) % PRINT_INTERVAL == 0:
            print(f"{((idx + 1) / total):2f} or {(idx + 1)} / {total}")
    dataset.to_csv("completions.csv", index=False)