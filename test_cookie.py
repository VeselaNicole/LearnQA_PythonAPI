import requests

class TestCookie:
    def test_cookie_value(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie_value = dict(response.cookies)
        print(cookie_value)
        assert response.status_code == 200, "Status code is not correct"
        assert "HomeWork" in cookie_value, "there is no cookie 'HomeWork' in received cookies"
        assert cookie_value["HomeWork"] == "hw_value", "cookie value is incorrect"