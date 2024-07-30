from pages.cart_page import CartPage
from pages.product_page import ProductPage


def test_open_cart_page(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()


def test_continue_shopping_btn(login):
    driver = login
    cart_page = CartPage(driver)
    test_open_cart_page(login)
    cart_page.click_continue_shopping_btn()


def test_add_to_cart_1_item(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.add_to_cart()


def test_add_to_cart_6_items(login):
    driver = login
    product_page = ProductPage(driver)
    product_page.add_to_cart_all_items()
    cart_page = CartPage(driver)
    cart_page.verify_items_in_the_cart()


def test_remove_from_cart(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    cart_page.remove_item_from_cart()


def test_item_has_price(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    cart_page.verify_price_item()


def test_verify_checkout_btn(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    cart_page.verify_checkout_btn_visible()

