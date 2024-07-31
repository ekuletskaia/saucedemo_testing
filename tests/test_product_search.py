from pages.product_page import ProductPage


# verify title on the page

def test_title_on_the_page(login):
    product_page = ProductPage(login)
    product_page.verify_title()


# verify 6 product card on the page

# verify that all product cards has price

# verify all product cards has add to cart button

# verify all product cards has title

# verify all product cards has discription

# verify the cart icon presence when add to cart item

# verify cart badge

# verify the filter presence

# verify filter A to Z
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


# verify menu select about
def test_verify_menu_about(login):
    product_page = ProductPage(login)
    product_page.verify_menu_about()
