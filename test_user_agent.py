import requests
import pytest

class TestUserAgent:
    user_agents = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
    ]
    @pytest.mark.parametrize("user_agent", user_agents)
    def test_user_agent(self, user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)

        assert response.status_code == 200, "Status code is incorrect"


        assert 'platform' in response.json(), "There is no field 'platform' in response"
        assert 'browser' in response.json(), "There is no field 'browser' in response"
        assert 'device' in response.json(), "There is no field 'device' in response"
        actual_platform_value = response.json()['platform']
        actual_browser_value = response.json()['browser']
        actual_device_value = response.json()['device']

        if user_agent == 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30':
            expected_platform_value = "Mobile"
            expected_browser_value = "No"
            expected_device_value = "Android"

        if user_agent == 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1':
            expected_platform_value = "Mobile"
            expected_browser_value = "Chrome"
            expected_device_value = "iOS"

        if user_agent == 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)':
            expected_platform_value = "Googlebot"
            expected_browser_value = "Unknown"
            expected_device_value = "Unknown"

        if user_agent == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0':
            expected_platform_value = "Web"
            expected_browser_value = "Chrome"
            expected_device_value = "No"

        if user_agent == 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1':
            expected_platform_value = "Mobile"
            expected_browser_value = "No"
            expected_device_value = "iPhone"


        assert actual_platform_value == expected_platform_value, f"for user-agent {user_agent} actual platform  {actual_platform_value} is not equal to {expected_platform_value}"
        assert actual_browser_value == expected_browser_value, f"for user-agent {user_agent} actual browser {actual_browser_value} is not equal to {expected_browser_value}"
        assert actual_device_value == expected_device_value, f"for user-agent {user_agent} actual device {actual_device_value} is not equal to {expected_device_value}"