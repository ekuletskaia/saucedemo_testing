from pages.logout_page import LogoutPage


def test_logout(login):
    driver = login
    logout_page = LogoutPage(driver)
    logout_page.logout()
