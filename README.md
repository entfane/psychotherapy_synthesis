# Emotional Prompt Synthesis Dataset Generator

This project generates a synthetic dataset of user prompts paired with emotional states and optional AI responses. The dataset is designed for training and evaluating emotionally-aware AI systems.

## Features

- Generates diverse user prompts based on scenario templates
- Associates each prompt with an emotional state description
- Optionally generates AI responses to the prompts
- Uses OpenAI and/or Google APIs for text generation

## Prerequisites

- Python 3.12
- Poetry (for dependency management)
- OpenAI API key
- Google API key

## Setup

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file in the project root with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. Prepare your scenarios in `scenarios.txt` (one scenario per line)

## Usage

### Generate Prompt-Emotion Dataset

To generate a dataset of prompts with emotional states:
```bash
poetry run python main.py
```

### Generate Responses (Optional)

To extend the dataset with AI-generated responses:
```bash
poetry run python completion_generation.py
```

### Configuration

- Edit `scenarios.txt` to modify the base scenarios used for prompt generation

## Output Format (CSV)  

The generated dataset will be in CSV format with the following columns:  

| Column       | Description                          | Example |  
|--------------|--------------------------------------|---------|  
| `prompt`     | Generated user prompt                | "Why does this app keep crashing when I try to save my work?" |  
| `emotion`    | Description of user's emotional state | "Frustrated and anxious about losing progress" |  
| `response`   | Generated AI response (if generated) | "I'm sorry to hear that. Let me help troubleshoot..." |  

Example CSV output:  
```csv  
prompt,emotion,response  
"I love the new dark mode! It's so easy on my eyes.","Excited and satisfied with the improvement","That's great to hear! We designed it for better readability."  
```  
