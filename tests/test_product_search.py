from pages.product_page import ProductPage


def test_title_on_the_page(login):
    product_page = ProductPage(login)
    product_page.verify_title()


def test_product_cards_have_title_desc_price(login):
    product_page = ProductPage(login)
    product_page.verify_all_products_have_title_desc_price()


def test_cart_icon_presence(login):
    product_page = ProductPage(login)
    product_page.verify_cart_icon()


def test_cart_badge_when_click_add_to_cart(login):
    product_page = ProductPage(login)
    product_page.verify_cart_badge_number()


def test_filter_presence(login):
    product_page = ProductPage(login)
    product_page.verify_filter_on_the_page()


def test_verify_filter_az(login):
    product_page = ProductPage(login)
    product_page.verify_filter_az()


def test_verify_filter_za(login):
    product_page = ProductPage(login)
    product_page.verify_filter_za()


def test_verify_filter_lohi(login):
    product_page = ProductPage(login)
    product_page.verify_filter_lohi()


def test_verify_filter_hilo(login):
    product_page = ProductPage(login)
    product_page.verify_filter_hilo()


def test_verify_menu_about(login):
    product_page = ProductPage(login)
    product_page.verify_menu_about()
