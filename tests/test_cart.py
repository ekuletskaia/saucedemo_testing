from pages.cart_page import CartPage


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

# add 6 items in the cart and verify that 6 items are in the cart