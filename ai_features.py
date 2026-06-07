from openai import OpenAI
from dotenv import load_dotenv
import os

#load environment vaiables
load_dotenv()

# get API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("WARNING: OPENROUTER_API_KEY not found in .env file!")

# openrouter client
client = OpenAI(
    api_key = API_KEY,
    base_url = "https://openrouter.ai/api/v1"
)

# ====================== ask ai functions ========================

def ask_ai_stream(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI resume assistant. Give professional and concise answer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=500,
        stream=True
    )

    for event in response:
        if not getattr(event, "choices", None):
            continue

        delta = event.choices[0].delta
        if not delta:
            continue

        content = getattr(delta, "content", None)
        if content:
            yield content


def ask_ai(prompt):
    try:
        return "".join(ask_ai_stream(prompt))
    except Exception:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI resume assistant. Give professional and concise answer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=700
        )
        return response.choices[0].message.content
