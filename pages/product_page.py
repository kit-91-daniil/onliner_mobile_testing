from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators
from utils.page_helper import PageHelper


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        self.helper = PageHelper(self.browser)

    def verify_product_title_correctness(self, product_name):
        product_title = self.helper.get_element_text(*ProductPageLocators.PRODUCT_TITLE)
        assert product_name in product_title, "Product page header des not contain product name"

    def order_the_product(self):
        self.add_product_to_the_cart()
        self.go_to_cart_page()

    def close_product_sidebar(self):
        if self.helper.is_element_present(*ProductPageLocators.CLOSE_IFRAME_BUTTON):
            self.helper.click_on_active_element(*ProductPageLocators.CLOSE_IFRAME_BUTTON)

    def add_product_to_the_cart(self):
        self.helper.click_on_active_element(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def go_to_product_cart(self):
        self.helper.click_on_active_element(*ProductPageLocators.GO_TO_CART_BUTTON)

    def go_to_cart_page(self):
        self.close_product_sidebar()
        self.browser.refresh()

        self.helper.click_on_active_element(*ProductPageLocators.GO_TO_CART_BUTTON)
