from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from pages.base_page import Page


class SocialMediaLinksPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.twitter = (By.CSS_SELECTOR, 'li.social_twitter')
        self.facebook = (By.CSS_SELECTOR, 'li.social_facebook')
        self.linkedin = (By.CSS_SELECTOR, 'li.social_linkedin')
        self.popup_button = (By.CSS_SELECTOR, "icon.contextual-sign-in-modal__modal-dismiss-icon")

    def handle_alert(self):
        try:
            alert = Alert(self.driver)
            alert.dismiss()  # or alert.accept() based on your need
        except:
            pass  # If no alert is present, ignore the exception

    def verify_twitter_link(self):
        self.click(*self.twitter)
        self.switch_to_new_window()
        self.handle_alert()
        self.verify_url_matches('https://x.com/saucelabs')

    def verify_facebook_link(self):
        self.click(*self.facebook)
        self.switch_to_new_window()
        self.handle_alert()
        self.verify_url_matches('https://www.facebook.com/saucelabs')

    def verify_linkedin_link(self):
        self.click(*self.linkedin)
        self.switch_to_new_window()
        self.handle_alert()
        self.verify_url_matches('https://www.linkedin.com/company/sauce-labs/')

