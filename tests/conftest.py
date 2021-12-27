import time
import pytest
from appium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import DriverConfig as Config


@pytest.fixture(scope="function")
def browser():
    web_browser = webdriver.Remote(Config.command_executor, Config.desired_capability)
    time.sleep(Config.launching_timeout)  # Probably it should not be used here
    yield web_browser
    web_browser.quit()


# def pytest_addoption(parser):
#     parser.addoption("--language", action="store", default="en", help="choose language: es or en or ru")
#     parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="class")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     language = request.config.getoption("language")
#     browser = None
#     if browser_name == "chrome":
#         options = Options()
#         options.add_argument("--window-size=1600,1250")
#         options.add_experimental_option('prefs', {'intl.accept_languages': language})
#         browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
#
#     elif browser_name == "firefox":
#         fp = webdriver.FirefoxProfile()
#         fp.set_preference("intl.accept_languages", language)
#         browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
#     else:
#         raise pytest.UsageError("--browser name should be chrome or firefox")
#     yield browser
#     browser.quit()
