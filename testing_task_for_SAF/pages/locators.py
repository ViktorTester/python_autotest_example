from selenium.webdriver.common.by import By


class LoginPageLocators:
    CORRECT_LOGIN = (By.ID, "user-name")
    CORRECT_PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login-button']")
    WRONG_CREDS_MSG = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    CORRECT_CREDS = (By.CLASS_NAME, "shopping_cart_link")
