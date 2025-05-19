import os
import requests

class LLMModels:
    def __init__(self):
        self.models = []
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('API_KEY')}",
            "Content-Type": "application/json"
        }
        self.url = "https://api.groq.com/openai/v1/models"
        self.request_model()

    def get_models(self):
        return self.models

    def get_model(self, model_name):
        return self.models[model_name]

    def request_model(self):
        response = requests.get(self.url, headers=self.headers)
        response_data = response.json()['data']
        response_model_names = [x['id'] for x in response_data]

        self.models = response_model_names
        
