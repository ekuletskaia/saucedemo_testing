from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, "title")
        self.logout_button = (By.ID, "logout-button")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()
