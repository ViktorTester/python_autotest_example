import pytest
from selenium import webdriver


def pytest_adoption(parser):
    parser.addoption('--browser_name', default='safari')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "safari":
        print("\nstart browser safari for test...")
        browser = webdriver.Safari()
        browser.maximize_window()
    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))
    yield browser
    print("\nquit browser...")
    browser.quit()
