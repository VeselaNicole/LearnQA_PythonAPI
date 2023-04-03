import requests


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
