import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


url_get_cookie = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_login = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
url_table_of_passwords = "https://www.wikiwand.com/en/List_of_the_most_common_passwords"


def test_password_guessing():

    for password in get_passwords():
        params = {"login": "super_admin", "password": password}
        response = requests.post(url_get_cookie, params=params)
        cookie_value = response.cookies["auth_cookie"]
        response_auth = requests.post(url_login, cookies={"auth_cookie": cookie_value})
        if response_auth.text != "You are NOT authorized":
            print(f"{response_auth.text} which means the password is '{password}'")
            break


def get_passwords():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url_table_of_passwords)

    wikitable_elements = driver.find_elements(By.CLASS_NAME, "wikitable")[1]
    tbody = wikitable_elements.find_element(By.TAG_NAME, "tbody")
    passwords = []
    rows = tbody.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the first row (headers)
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")[
            1:
        ]

        for column in columns:
            value = column.text
            passwords.append(value)

    driver.quit()
    return passwords
