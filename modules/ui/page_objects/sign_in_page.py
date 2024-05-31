from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'


    def __init__(self) -> None:
        super().__init__()

    
    def go_to(self):
        self.driver.get(SignInPage.URL)


    def try_login(self, username, password):
        #Пошук елементу логін та введення його
        login_elem = self.driver.find_element(By.ID, 'login_field')
        login_elem.send_keys(username)

        # Пошук елементу пасворд та введення його
        login_pass = self.driver.find_element(By.ID, 'password')
        login_pass.send_keys(password)

        #Пошук елементу "Вхід" та відправка даних
        butt_elem = self.driver.find_element(By.NAME, 'commit')
        butt_elem.click()

    def check_tittle(self, expected_title):
        return self.driver.title == expected_title