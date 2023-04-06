import requests

response = requests.get("https://www.learnqa.ru/tpost/9rgayjrhrk-pro-model-osi-bistro-i-prosto")
print(response.text)