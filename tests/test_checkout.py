def test_verify_checkout_page(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_checkout_url_page()


def test_continue_btn_presence(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_continue_btn()


def test_cancel_btn_presence(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_cancel_btn()


def test_checkout_form_presence(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_checkout_form()


def test_checkout_first_step_happy_path(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_checkout_form_info()


def test_verify_cancel_btn_works(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_cancel_btn_move_back_to_cart()


def test_error_message_displayed_empty_fields(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_error_message_empty_fields()


def test_error_msg_displayed_empty_fname_field(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_error_message_empty_fn_field()


def test_error_msg_displayed_empty_lname_field(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_error_message_empty_ln_field()


def test_error_msg_displayed_empty_zipcode_field(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_error_message_empty_zip_field()


def test_checkout_second_step(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_happy_path_checkout_second_step()


def test_verify_back_home_btn_visible(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_back_home_btn_presence()


def test_verify_total_price_displayed(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_total_price_displayed()


def test_verify_back_home_btn_works(setup_cart_and_checkout):
    checkout_page = setup_cart_and_checkout
    checkout_page.verify_back_home_btn_moves_to_products()

