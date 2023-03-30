import json
from json.decoder import JSONDecodeError
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
key_1 = "messages"
key_2 = "message"
try:
    json_obj = json.loads(json_text)
    if key_1 in json_obj:
        if key_2 in json_obj[key_1][1]:
            print(json_obj[key_1][1][key_2])
        else:
            print(f"Поля {key_2} в JSON нет")
    else:
        print(f"Поля {key_1} в JSON нет")
except JSONDecodeError:
    print("Response in not JSON")