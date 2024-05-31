import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://github.com/login")

    #Пошук елементу логін та введення його
    login_elem = driver.find_element(By.ID, 'login_field')
    login_elem.send_keys("segiibutenko@mistakeinname.com")

    # Пошук елементу пасворд та введення його
    login_pass = driver.find_element(By.ID, 'password')
    login_pass.send_keys("wrong password")
    
    #Пошук елементу "Вхід" та відправка даних
    butt_elem = driver.find_element(By.NAME, 'commit')
    butt_elem.click()
    #Перевірка що назва сторінки відповідає очікуванню
    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
