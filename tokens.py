import requests
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response1.json()["token"]
seconds = response1.json()["seconds"]
print(response1.text)
print(token)
print(seconds)

#time.sleep(seconds)
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
print(response2.text)
if response2.json()["status"] == "Job is NOT ready":
    print(f"Please wait for {seconds} seconds")
    time.sleep(seconds)
    response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    if response3.json()["status"] == "Job is ready" and "result" in response3.text:
        print(response3.json()["result"])
    else:
        print("Error in process")
elif response2.json()["status"] == "Job is ready":
    print(response2.json()["result"])
else:
    print("Incorrect status")