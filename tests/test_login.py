from utils.config import BASE_URL, INVALID_USERNAME, INVALID_PASSWORD
from pages.login_page import LoginPage


def test_valid_login(login):
    driver = login
    assert "Swag Labs" in driver.title


def test_invalid_login(setup_browser):
    driver = setup_browser
    login_page = LoginPage(driver)
    driver.get(BASE_URL)
    login_page.enter_username(INVALID_USERNAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_login_button()

    error_message = login_page.get_error_message()
    print(f"Error message: {error_message}")
    assert "Epic sadface" in error_message
