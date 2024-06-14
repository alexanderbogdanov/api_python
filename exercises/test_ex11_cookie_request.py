import requests


def test_cookie_request():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

    for cookie_name, cookie_value in response.cookies.items():
        print(f"Cookie: {cookie_name}, Value: {cookie_value}")

    assert "HomeWork" in response.cookies, "HomeWork cookie is not set"
    assert (
        response.cookies.get("HomeWork") == "hw_value"
    ), "HomeWork cookie value is not correct"
