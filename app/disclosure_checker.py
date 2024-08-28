import openai
import os
from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

def check_disclosure_with_llm(page_text: str, disclosure_text: str) -> bool:
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = (
        f"Given the following webpage content:\n\n{page_text}\n\n"
        f"Does this webpage contain the following disclosure or a semantically similar statement?\n\n"
        f"Disclosure: \"{disclosure_text}\""
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a compliance assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,
        )

        print(response)
        # Extract the response text
        result = response['choices'][0]['message']['content'].strip().lower()
        print(result)
        return "yes" in result
    except Exception as e:
        print(f"Error with LLM: {str(e)}")
        return False
