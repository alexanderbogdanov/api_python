import requests

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method_values = ["GET", "POST", "PUT", "DELETE", "HEAD"]
methods = ["get", "post", "put", "delete", "head"]


def test_compare_query_type():

    print("\n")
    for method in methods:
        for value in method_values:
            if method == "get":
                response_text = requests.request(
                    method, URL, params={"method": value}
                ).text
            else:
                response_text = requests.request(
                    method, URL, data={"method": value}
                ).text
            print(
                f"Response with a {method} method and {value} parameter: {response_text}"
            )
    print("\nChecking responses without 'method' parameter\n")

    # Checking responses without method parameter
    for method in methods:
        response = requests.request(method, URL).text
        print(f"Response without a 'method' parameter and with a {method.upper()} method: {response}")
