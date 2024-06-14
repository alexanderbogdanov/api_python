import pytest
import requests

user_agents = [
    (
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    ),
    (
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
    ),
    ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
    ),
    (
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    ),
]

expected_values = [
    {"platform": "Mobile", "browser": "No", "device": "Android"},
    {"platform": "Mobile", "browser": "Chrome", "device": "iOS"},
    {"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"},
    {"platform": "Web", "browser": "Chrome", "device": "No"},
    {"platform": "Mobile", "browser": "No", "device": "iPhone"},
]


@pytest.mark.parametrize("user_agent", user_agents)
def test_user_agent(user_agent):
    expected_platform = expected_values[user_agents.index(user_agent)]["platform"]
    expected_browser = expected_values[user_agents.index(user_agent)]["browser"]
    expected_device = expected_values[user_agents.index(user_agent)]["device"]

    response = requests.get(
        "https://playground.learnqa.ru/ajax/api/user_agent_check",
        headers={"User-Agent": user_agent},
    )
    actual_platform = response.json()["platform"]
    actual_browser = response.json()["browser"]
    actual_device = response.json()["device"]
    print(
        f"\n platform is: {actual_platform}, \n browser is: {actual_browser}, \n device is: {actual_device}"
    )
    assert (
        actual_platform == expected_platform
    ), f"Platform should be '{expected_platform}' but got '{actual_platform}'"
    assert (
        actual_browser == expected_browser
    ), f"Browser should be '{expected_browser}' but got '{actual_browser}'"
    assert (
        actual_device == expected_device
    ), f"Device should be '{expected_device}' but got'{actual_device}'"
