import requests


def test_header_request():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    print(response.headers)
    assert "x-secret-homework-header" in response.headers, "Header is not set"
    expected_value = "Some secret value"
    actual_value = response.headers.get("x-secret-homework-header")
    assert actual_value == expected_value, "Header value is not correct"
