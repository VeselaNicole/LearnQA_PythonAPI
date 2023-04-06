import requests

class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Nicole"
        params = {"name": name}
        response = requests.get(url, params=params)

        assert response.status_code == 200, "Wrong status code"

        #response_dict = response.json()
        assert "answer" in response.json(), "There is no field 'answer' in response"

        #expected_text = f"Hello, {name}"
        #actual_text = response_dict["answer"]
        assert response.json()["answer"] == f"Hello, {name}", "Actual text in response is not correct"