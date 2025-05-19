import os
from openai import OpenAI

class Chat:
    def __init__(self, model_name):
        self.model_name = model_name
        self.content = ""
        self.client = self.client()

    def client(self):
        return OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("API_KEY"),
        )
    
    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content
    
    def completion(self, content):
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model=self.model_name,
        )
        
        content = chat_completion.choices[0].message.content

        self.set_content(content)
        return self.get_content()