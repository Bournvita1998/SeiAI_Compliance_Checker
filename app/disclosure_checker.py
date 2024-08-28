import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def check_disclosure_with_llm(page_text: str, disclosure_text: str) -> bool:
    prompt = (
        f"Given the following webpage content:\n\n{page_text}\n\n"
        f"Does this webpage contain the following disclosure or a semantically similar statement?\n\n"
        f"Disclosure: \"{disclosure_text}\""
    )

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a compliance assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=100)

        # Extract the response text
        result = response.choices[0].message.content.strip().lower()
        return "yes" in result
    except Exception as e:
        print(f"Error with LLM: {str(e)}")
        return False
