from selenium.webdriver.common.by import By
from pages.base_page import Page
from utils.config import FIRST_NAME, LAST_NAME, ZIP_CODE, SUCCESS_MSG


class CheckoutPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.ID, "checkout")
        self.checkout_info = (By.CSS_SELECTOR, "div.checkout_info")
        self.continue_btn = (By.ID, "continue")
        self.cancel_btn = (By.ID, "cancel")
        self.error_message = (By.CSS_SELECTOR, "div.error-message-container")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.finish_btn = (By.ID, "finish")
        self.success_msg = (By.CSS_SELECTOR, "h2.complete-header")
        self.back_home_btn = (By.ID, "back-to-products")
        self.total_price = (By.CSS_SELECTOR, "div.summary_total_label")

    def verify_checkout_url_page(self):
        self.click(*self.checkout_btn)
        self.verify_url_matches("https://www.saucedemo.com/checkout-step-one.html")

    def verify_continue_btn(self):
        self.click(*self.checkout_btn)
        self.verify_item_visible(*self.continue_btn)

    def verify_cancel_btn(self):
        self.click(*self.checkout_btn)
        self.verify_item_visible(*self.cancel_btn)

    def verify_checkout_form(self):
        self.click(*self.checkout_btn)
        self.verify_item_visible(*self.checkout_info)

    def verify_checkout_form_info(self):
        self.click(*self.checkout_btn)
        self.input_text(FIRST_NAME, *self.first_name_field)
        self.input_text(LAST_NAME, *self.last_name_field)
        self.input_text(ZIP_CODE, *self.zip_code_field)
        self.click(*self.continue_btn)
        self.verify_url_matches("https://www.saucedemo.com/checkout-step-two.html")

    def verify_error_message_empty_fields(self):
        self.click(*self.checkout_btn)
        self.click(*self.continue_btn)
        self.verify_item_visible(*self.error_message)

    def verify_error_message_empty_fn_field(self):
        self.click(*self.checkout_btn)
        self.input_text(LAST_NAME, *self.last_name_field)
        self.input_text(ZIP_CODE, *self.zip_code_field)
        self.click(*self.continue_btn)
        self.verify_item_visible(*self.error_message)

    def verify_error_message_empty_ln_field(self):
        self.click(*self.checkout_btn)
        self.input_text(FIRST_NAME, *self.last_name_field)
        self.input_text(ZIP_CODE, *self.zip_code_field)
        self.click(*self.continue_btn)
        self.verify_item_visible(*self.error_message)

    def verify_error_message_empty_zip_field(self):
        self.click(*self.checkout_btn)
        self.input_text(FIRST_NAME, *self.last_name_field)
        self.input_text(LAST_NAME, *self.last_name_field)
        self.click(*self.continue_btn)
        self.verify_item_visible(*self.error_message)

    def verify_happy_path_checkout_second_step(self):
        self.verify_checkout_form_info()
        self.click(*self.finish_btn)
        self.verify_text(SUCCESS_MSG, *self.success_msg)

    def verify_back_home_btn_presence(self):
        self.verify_happy_path_checkout_second_step()
        self.verify_item_visible(*self.back_home_btn)

    def verify_total_price_displayed(self):
        self.verify_checkout_form_info()
        self.verify_item_visible(*self.total_price)

    def verify_cancel_btn_move_back_to_cart(self):
        self.verify_checkout_url_page()
        self.click(*self.cancel_btn)
        self.verify_url_matches("https://www.saucedemo.com/cart.html")

    def verify_back_home_btn_moves_to_products(self):
        self.verify_back_home_btn_presence()
        self.click(*self.back_home_btn)
        self.verify_url_matches("https://www.saucedemo.com/inventory.html")

