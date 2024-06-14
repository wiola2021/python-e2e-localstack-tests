from selenium.webdriver.common.by import By
from components.alert import AlertComponent
from pages.abstract_base_page import AbstractBasePage

class SignupPage(AbstractBasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    confirm_password_input = (By.NAME, "confirm_password")
    signup_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
    error_alert = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def attempt_signup(self, username: str, password: str, confirm_password: str):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)
        self.driver.find_element(*self.signup_button).click()
        return self

    def get_alert(self):
        return AlertComponent(self.driver)