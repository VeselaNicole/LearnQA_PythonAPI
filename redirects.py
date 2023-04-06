import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response.history))
first_response = response.history[0]
second_response = response.history[1]
third_response = response
print(first_response.url)
print(second_response.url)
print(third_response.url)
