import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    STORY_GEN_SYSTEM_PROMPT = "You are a creative novelist. Based on the user’s input, create a captivating story within 400 characters."

    DEEPSEEK_URL = "http://localhost:11434/api/generate"
    DEEPSEEK_MODEL = "deepseek-r1:7b"

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing in .env file")