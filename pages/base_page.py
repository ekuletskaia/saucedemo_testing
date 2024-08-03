from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Page:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, url):
        """Open a given URL in the browser."""
        self.driver.get(url)

    def find_element(self, *locator):
        """Find a single element by locator."""
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """Find multiple elements by locator."""
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        """Click an element identified by locator."""
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        """Input text into an element identified by locator."""
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        """Wait until an element is clickable and then click it."""
        self.wait.until(EC.element_to_be_clickable(locator),
                        f'Element {locator} not clickable').click()

    def verify_item_visible(self, *locator):
        """Verify that an element is visible."""
        self.wait.until(EC.visibility_of_element_located(locator),
                        f'Element is not visible - {locator}')

    def verify_item_disappear(self, *locator):
        """Verify that an element is not visible."""
        self.wait.until(EC.invisibility_of_element(locator))

    def verify_url_contains(self, expected_text):
        """Verify that the current URL contains the expected text."""
        self.wait.until(EC.url_contains(expected_text)), f'URL does not contain {expected_text}'

    def verify_url_matches(self, expected_text):
        """Verify that the current URL matches the expected text."""
        self.wait.until(EC.url_matches(expected_text)), f'URL does not match with {expected_text}'

    def get_current_window(self):
        """Get the current window handle."""
        current_window = self.driver.current_window_handle
        return current_window

    def switch_to_new_window(self):
        """Switch to a newly opened window."""
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        """Switch to a window by its ID."""
        print('Switching to ...', window_id)
        self.driver.switch_to.window(window_id)

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.END)

    def verify_text(self, text, *locator):
        """Verify that an element's text matches the expected text."""
        actual_text = self.find_element(*locator).text
        assert text == actual_text, f'Error! {text} not in {actual_text}'

    def verify_partial_text(self, text, *locator):
        """Verify that an element's text contains the expected text."""
        actual_text = self.find_element(*locator).text
        assert text in actual_text, f'Error! {text} is not in {actual_text}'

    def save_screenshot(self, name):
        """Save a screenshot of the current page."""
        self.driver.save_screenshot(f'{name}.png')

    def close(self):
        """Close the current window."""
        self.driver.close()
