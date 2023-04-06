import requests

response = requests.put("https://playground.learnqa.ru/api/check_type", data={"name":"Nicole"})
print(response.text)