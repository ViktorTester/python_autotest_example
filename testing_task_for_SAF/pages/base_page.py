from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators
import time


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def correct_credentials(self):
        input1 = self.browser.find_element(*LoginPageLocators.CORRECT_LOGIN)
        input1.send_keys('standard_user')
        time.sleep(2)
        input2 = self.browser.find_element(*LoginPageLocators.CORRECT_PASSWORD)
        input2.send_keys('secret_sauce')
        time.sleep(2)
        link = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        link.click()

    def wrong_credentials(self):
        input1 = self.browser.find_element(*LoginPageLocators.CORRECT_LOGIN)
        input1.send_keys('wrong_login')
        time.sleep(2)
        input2 = self.browser.find_element(*LoginPageLocators.CORRECT_PASSWORD)
        input2.send_keys('test123')
        time.sleep(2)
        link = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        link.click()

    def should_be_wrong_credentials(self):
        assert self.is_element_present(*LoginPageLocators.WRONG_CREDS_MSG), "No error msg"

    def should_be_correct_credentials(self):
        assert self.is_element_present(
            *LoginPageLocators.CORRECT_CREDS), "No shopping_card presented. The user is still not logged in"
