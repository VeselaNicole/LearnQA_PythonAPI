import requests
payload = {"name": "Nicole"}
key = "answer"
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response = response.json()
print(parsed_response)
if key in parsed_response:
    print(parsed_response[key])
else:
    print(f"поля {key} в JSON нет")