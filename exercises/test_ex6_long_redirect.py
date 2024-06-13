import requests


def test_long_redirect():
    response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
    print(f"\n There are {len(response.history)} redirects")
    print(f"\n The first redirect URL is '{response.history[1].url}'")
    print(f"\n The second redirect URL is '{response.url}' which is also the final URL")



