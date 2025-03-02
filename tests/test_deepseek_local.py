import requests
import json

# Ollama API 엔드포인트
url = "http://localhost:11434/api/generate"

# 요청 데이터
data = {
    "model": "deepseek-r1:7b",
    "prompt": "Hello, how can I assist you?",
    "stream": False  # 스트리밍 여부 설정
}

# API 요청 보내기
response = requests.post(url, json=data)

# 응답 출력
if response.status_code == 200:
    result = response.json()
    print(result["response"])
else:
    print(f"Error: {response.status_code}, {response.text}")