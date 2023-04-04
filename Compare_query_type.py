import requests

response_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_1.text)

response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(response_2.text)
print(response_2.status_code)

response_3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print(response_3.text)
print(response_3.status_code)

request_types = ["GET", "POST", "PUT", "DELETE"]


for type in request_types:
    for param in request_types:
        if type == "GET":
            response = requests.request(type, "https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": f"{param}"})
        else:
            response = requests.request(type, "https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{param}"})
            if type != param and response.text == '{"success":"!"}':
                print(f"При типе запроса {type} и параметре {param} ошибочно выводится успешный ответ")
            if type == param and response.text != '{"success":"!"}':
                print(f"При типе запроса {type} и параметре {param} ошибочно выводится НЕуспешный ответ")
