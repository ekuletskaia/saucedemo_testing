from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page


class ProductPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.all_add_to_cart_btns = (By.CSS_SELECTOR, "button.btn_inventory")
        self.title_products = (By.CSS_SELECTOR, "span.title")
        self.cart_icon = (By.CSS_SELECTOR, "a.shopping_cart_link")
        self.cart_badge = (By.CSS_SELECTOR, "span.shopping_cart_badge")
        self.product_card_title = (By.CSS_SELECTOR, "div.inventory_item_name")
        self.product_card_price = (By.CSS_SELECTOR, "div.inventory_item_price")
        self.product_card_desc = (By.CSS_SELECTOR, "div.inventory_item_desc")
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.meny_about = (By.ID, "about_sidebar_link")
        self.filter = (By.CSS_SELECTOR, "select.product_sort_container")
        self.filter_name_az = (By.CSS_SELECTOR, 'option[value="az"]')
        self.filter_name_za = (By.CSS_SELECTOR, 'option[value="za"]')
        self.filter_price_lohi = (By.CSS_SELECTOR, 'option[value="lohi"]')
        self.filter_price_hilo = (By.CSS_SELECTOR, 'option[value="hilo"]')

    def add_to_cart_all_items(self):
        product_list = self.find_elements(*self.all_add_to_cart_btns)
        for button in product_list:
            button.click()

    def verify_title(self):
        self.verify_text("Products", *self.title_products)





    def verify_filter_az(self):
        dropdown_filter = self.find_element(*self.filter)
        select = Select(dropdown_filter)
        select.select_by_value("az")
        product_list = self.find_elements(*self.product_card_title)
        first_product_title = product_list[0].text
        assert first_product_title == "Sauce Labs Backpack", f'Error! Expected "Sauce Labs Backpack", but got {first_product_title}'

    def verify_filter_za(self):
        dropdown_filter = self.find_element(*self.filter)
        select = Select(dropdown_filter)
        select.select_by_value("za")
        product_list = self.find_elements(*self.product_card_title)
        first_product_title = product_list[0].text
        assert first_product_title == "Test.allTheThings() T-Shirt (Red)", f'Error! Expected "Sauce Labs Backpack", but got {first_product_title}'

    def verify_filter_lohi(self):
        dropdown_filter = self.find_element(*self.filter)
        select = Select(dropdown_filter)
        select.select_by_value("lohi")
        product_list = self.find_elements(*self.product_card_title)
        first_product_title = product_list[0].text
        assert first_product_title == "Sauce Labs Onesie", f'Error! Expected "Sauce Labs Backpack", but got {first_product_title}'

    def verify_filter_hilo(self):
        dropdown_filter = self.find_element(*self.filter)
        select = Select(dropdown_filter)
        select.select_by_value("hilo")
        product_list = self.find_elements(*self.product_card_title)
        first_product_title = product_list[0].text
        assert first_product_title == "Sauce Labs Fleece Jacket", f'Error! Expected "Sauce Labs Backpack", but got {first_product_title}'

    def verify_menu_about(self):
        self.click(*self.menu_btn)
        self.click(*self.meny_about)
        self.verify_url_matches("https://saucelabs.com/")