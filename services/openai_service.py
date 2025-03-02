import openai
from config import Config


class OpenAIService:
    def __init__(self):
        Config.validate()
        self.api_key = Config.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def generate_story(self, prompt: str) -> str:
        """
        사용자 입력을 기반으로 소설을 생성하는 메서드
        """
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": Config.STORY_GEN_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def translate_text(self, text: str, target_language: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": f"Translate the following text into {target_language}:"},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"