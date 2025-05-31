from prompts import EMOTIONAL_DESCRIPTION_SYSTEM_PROMPT, EMOTIONAL_DESCRIPTION_USER_PROMPT, PROMPT_GENERATION_SYSTEM_PROMPT, PROMPT_GENERATION_USER_PROMPT
from response_generator import ResponseGenerator
from utils import txt_to_list
import pandas as pd

SCENARIOS_PATH = 'scenarios.txt'
NUMBER_OF_PROMPTS_PER_SCENARIO = 5
MAX_EMOTIONAL_DESCRIPTIONS_PER_PROMPT = 3
PRINT_INTERVAL = 10


if __name__ == "__main__":
    LLM = ResponseGenerator()
    scenarios = txt_to_list(SCENARIOS_PATH)
    total_to_generate = len(scenarios) * NUMBER_OF_PROMPTS_PER_SCENARIO * MAX_EMOTIONAL_DESCRIPTIONS_PER_PROMPT
    dataset = pd.DataFrame(columns=["prompt", "emotional_description"])
    record_num = 1
    for scenario in scenarios:
        prompts = []
        for prompt_num in range(NUMBER_OF_PROMPTS_PER_SCENARIO):
            input_user_prompt = PROMPT_GENERATION_USER_PROMPT.format(scenario=scenario, mentioned="\n".join(prompts))
            prompt = LLM.generate_gemini_response(PROMPT_GENERATION_SYSTEM_PROMPT, input_user_prompt)
            prompts.append(prompt)
            emotional_descriptions = []
            for emotion_num in range(MAX_EMOTIONAL_DESCRIPTIONS_PER_PROMPT):
                emotion_description_user_prompt = EMOTIONAL_DESCRIPTION_USER_PROMPT.format(input = prompt,
                                                                                            mentioned="\n".join(emotional_descriptions))
                emotional_description = LLM.generate_gemini_response(EMOTIONAL_DESCRIPTION_SYSTEM_PROMPT, emotion_description_user_prompt)
                emotional_descriptions.append(emotional_description)
                new_record = {
                    "prompt": prompt,
                    "emotional_description": emotional_description,
                }
                dataset.loc[len(dataset)] = new_record
                if record_num % PRINT_INTERVAL == 0:
                    print(f"{record_num / total_to_generate} or {record_num} / {total_to_generate}")
                record_num += 1
    dataset.to_csv('dataset.csv', index=False)

            
                


    
    
    
