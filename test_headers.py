import requests

class TestHeaders:
    def test_headers_value(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.headers)
        assert response.status_code == 200, "Status code is incorrect"
        assert 'x-secret-homework-header' in response.headers, "No secret headers in headers"
        actual_header_value = response.headers['x-secret-homework-header']
        expected_header_value = "Some secret value"
        assert expected_header_value == actual_header_value, f"Actual secret header value is not {expected_header_value}"