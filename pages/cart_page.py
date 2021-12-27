from .base_page import BasePage
from .locators import CartPageLocators
from utils.page_helper import PageHelper


class CartPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CartPage, self).__init__(*args, **kwargs)
        self.helper = PageHelper(self.browser)

    def verify_product_is_in_cart(self, product_name):
        product_locator = CartPageLocators.get_product_locator(product_name)
        product_text = self.helper.get_element_text(*product_locator)
        assert product_name in product_text, f"There is no product with name '{product_name}' in the cart"

    def delete_product_from_the_cart(self):
        self.helper.click_on_active_element(*CartPageLocators.REMOVE_BUTTON)

    def verify_cart_is_empty(self):
        assert self.helper.is_not_element_present(*CartPageLocators.INCREMENT_PRODUCT_BUTTON)
