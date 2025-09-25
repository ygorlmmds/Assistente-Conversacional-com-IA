import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(user_msg):
    completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": user_msg}]
    )
    return completion.choices[0].message["content"]
