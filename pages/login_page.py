from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "div.error-message-container")

    def login(self, username, password):
        self.input_text(username, *self.username_field)
        self.input_text(password, *self.password_field)
        self.click(*self.login_button)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
