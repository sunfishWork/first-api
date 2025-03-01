import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing in .env file")

        self.client = openai.OpenAI(api_key=self.api_key)  # 최신 방식

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(  # 최신 방식
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content  # 최신 방식
        except Exception as e:
            return f"Error: {str(e)}"

    def generate_story(self, prompt: str) -> str:
        """
        사용자 입력을 기반으로 소설을 생성하는 메서드
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 창의적인 소설 작가입니다. 사용자의 입력을 바탕으로 매력적인 이야기를 만들어 주세요."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
