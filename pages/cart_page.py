from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_btn = (By.CSS_SELECTOR, "a.shopping_cart_link")
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        self.add_to_cart_btn_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_item = (By.CSS_SELECTOR, "div.cart_item")
        self.remove_btn = (By.ID, "remove-sauce-labs-backpack")
        self.item_price_in_the_cart = (By.CSS_SELECTOR, "div.inventory_item_price")
        self.checkout_btn = (By.ID, "checkout")

    def go_to_cart_page(self):
        self.click(*self.cart_btn)
        self.verify_url_matches("https://www.saucedemo.com/cart.html")

    def click_continue_shopping_btn(self):
        self.click(*self.continue_shopping_btn)
        self.verify_url_matches("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.wait_until_clickable_click(*self.add_to_cart_btn_backpack)
        self.click(*self.cart_btn)
        self.verify_item_visible(*self.cart_item)

    def verify_items_in_the_cart(self):
        self.go_to_cart_page()
        item_list = self.find_elements(*self.cart_item)
        print(f'Items in the cart:{len(item_list)}')
        assert len(item_list) == 6, "There should be 6 items in the cart"

    def remove_item_from_cart(self):
        self.click(*self.remove_btn)
        self.verify_item_disappear(*self.cart_item)

    def verify_price_item(self):
        self.verify_item_visible(*self.item_price_in_the_cart)

    def verify_checkout_btn_visible(self):
        self.verify_item_visible(*self.checkout_btn)

