from .pages.main_page import MainPage

link = "https://www.saucedemo.com/"


def test_user_should_not_login(browser):
    page = MainPage(browser, link)
    page.open()
    page.wrong_credentials()
    page.should_be_wrong_credentials()


def test_user_should_successfully_login(browser):
    page = MainPage(browser, link)
    page.open()
    page.correct_credentials()
    page.should_be_correct_credentials()
