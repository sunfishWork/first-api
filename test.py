import requests

url = "http://127.0.0.1:5000/openai/query"
headers = {"Content-Type": "application/json"}
data = {"prompt": "hello"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("응답:", response.json()["response"])
else:
    print("오류:", response.json())

