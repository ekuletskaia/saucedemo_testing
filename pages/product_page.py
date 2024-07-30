from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.all_add_to_cart_btns = (By.CSS_SELECTOR, "button.btn_inventory")

    def add_to_cart_all_items(self):
        product_list = self.find_elements(*self.all_add_to_cart_btns)
        for button in product_list:
            button.click()

