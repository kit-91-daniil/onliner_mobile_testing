from .base_page import BasePage
from .locators import MainPageLocators
from utils.page_helper import PageHelper
from utils.logger import logger


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.helper = PageHelper(self.browser)

    def verify_logo_presence(self):
        self.helper.find_element(*MainPageLocators.LOGO)

    def go_to_the_cart_page(self):
        self.helper.click_on_active_element(*MainPageLocators.DROP_DOWN_MENU_BUTTON)
        self.helper.click_on_active_element(*MainPageLocators.CART_MOBILE_BUTTON)

    def search_product_by_name(self, product):
        search_input = self.helper.find_element(*MainPageLocators.PRODUCT_FAST_SEARCH_INPUT)
        search_input.send_keys(product)
        logger.info(f"Sending keys {product}")

    def find_product(self, product):
        self.search_product_by_name(product)
        # iframe = self.helper.find_element(*MainPageLocators.IFRAME)
        # self.browser.switch_to.frame(iframe)
        product_link_locator = MainPageLocators.get_product_link_locator(product)
        self.helper.click_on_active_element(*product_link_locator)
