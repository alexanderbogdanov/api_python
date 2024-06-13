import requests
import time

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"


def test_longtime_job():
    response_get_token = requests.get(URL)
    params = response_get_token.json()
    # params = {"token": response_get_token.json()["token"]}
    time_in_seconds = response_get_token.json()["seconds"]
    print(response_get_token.text)
    print(response_get_token.json())
    response_with_token_before_task_done = requests.get(URL, params=params)
    status = response_with_token_before_task_done.json()["status"]
    assert status == "Job is NOT ready"  # check if the job is not ready
    print(response_with_token_before_task_done.text)
    time.sleep(time_in_seconds)

    response_with_token = requests.get(URL, params=params)
    status = response_with_token.json()["status"]
    assert status == "Job is ready"
    assert "result" in response_with_token.json()
    print(response_with_token.text)
