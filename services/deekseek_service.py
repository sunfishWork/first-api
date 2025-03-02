import requests
from config import Config


class DeepSeekService:
    def __init__(self):
        Config.validate()
        self.url = Config.DEEPSEEK_URL
        # self.api_key = Config.OPENAI_API_KEY
        # self.client = openai.OpenAI(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        try:
            data = {
                "model": Config.DEEPSEEK_MODEL,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(self.url, json=data)
            if response.status_code == 200:
                return response.json().get("response")
        except Exception as e:
            return f"Error: {str(e)}"
