from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import logger
from appium.webdriver.common.appiumby import AppiumBy


class PageHelper:
    def __init__(self, browser):
        self.browser = browser

    def click_on_visible_element(self, how, what, timeout=10):
        WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located((how, what))).click()
        logger.info(f"Element {how} - {what} has been clicked")

    def click_on_active_element(self, how, what, timeout=10):
        logger.info(f"Trying to click lement {how} - {what}")
        WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable((how, what))).click()
        logger.info(f"Element {how} - {what} has been clicked")

    def get_clicked_element(self, how, what, timeout=10):
        logger.info(f"Trying to find and click on element {how} - {what} has been clicked")
        element = WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable((how, what)))
        element.click()
        logger.info(f"Element {how} - {what} has been clicked")
        return element

    def find_element(self, how, what, timeout=10):
        logger.info(f"Trying to find element {how} - {what}")
        return WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((how, what)))

    def find_element_by_text(self, text):
        xpass_element_locator = AppiumBy.XPATH, "//.[@text='{text}']".format(text=text)
        return self.find_element(*xpass_element_locator)

    def get_element_text(self, how, what, timeout=10) -> str:
        logger.info(f"Trying to find element {how} - {what} and get element.text")
        return WebDriverWait(self.browser, timeout=timeout).until(
            EC.presence_of_element_located((how, what))).text

    def is_element_disappeared(self, how, what, timeout=10) -> bool:
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout=timeout, poll_frequency=1, ignored_exceptions=TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        return True

    def is_element_present(self, how, what, timeout=10) -> bool:
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        return True

    def is_element_has_a_text(self, how, what, timeout=10):
        try:
            logger.info(f"Trying to find element {how} - {what}")
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        result = element.text if hasattr(element, "text") else True
        return result

    def is_not_element_present(self, how, what, timeout=10):
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return True
        return False
