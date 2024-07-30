from selenium.webdriver.common.by import By
from pages.base_page import Page


class LogoutPage(Page):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.menu_btn = (By.ID, 'react-burger-menu-btn')
        self.logout_btn = (By.ID, 'logout_sidebar_link')
        self.login_btn = (By.ID, 'login-button')

    def logout(self):
        self.click(*self.menu_btn)
        self.click(*self.logout_btn)
        self.verify_item_visible(*self.login_btn)


