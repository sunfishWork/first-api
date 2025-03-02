import requests

url = "http://127.0.0.1:5000/deepseek/query"
headers = {"Content-Type": "application/json"}
data = {"prompt": "오늘은 너에게 어떤 하루지?"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("응답:", response.json()["response"])
else:
    print("오류:", response.json())

