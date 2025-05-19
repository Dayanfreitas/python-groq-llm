import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq

import requests

load_dotenv()


headers = {
    "Authorization": f"Bearer {os.environ.get('API_KEY')}",
    "Content-Type": "application/json"
}


url = "https://api.groq.com/openai/v1/models"

response = requests.get(url, headers=headers)
response_data = response.json()['data']
response_model_names = [x['id'] for x in response_data]

print(response_model_names)


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("API_KEY"),
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Oi, como você está?",
        }
    ],
    model="llama-3.3-70b-versatile",
)
