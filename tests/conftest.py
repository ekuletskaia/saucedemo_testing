import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def setup_browser():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    # Add any desired options here, e.g., headless mode
    # chrome_options.add_argument("--headless")

    driver_path = ChromeDriverManager().install()
    service = ChromeService(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture
def login(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()


@pytest.fixture
def setup_cart_and_checkout(login):
    driver = login
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    checkout_page = CheckoutPage(driver)
    return checkout_page
