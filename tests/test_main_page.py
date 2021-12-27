import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from tests.data.payload import Payload
from config.urls import Urls


class TestMainPage:
    @pytest.mark.logo_presence
    def test_user_can_see_logo(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.verify_logo_presence()

    @pytest.mark.verify_empty_cart
    def test_cart_should_be_empty(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.go_to_the_cart_page()
        cart_page = CartPage()
        cart_page.verify_cart_is_empty()

    @pytest.mark.product_search
    @pytest.mark.parametrize("product", Payload.PRODUCTS_FOR_SEARCH)
    def test_user_can_find_the_product(self, browser, product):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.find_product(product)
        product_page = ProductPage(browser, browser.current_url)
        product_page.verify_product_title_correctness(product)

    @pytest.mark.add_product
    @pytest.mark.parametrize("product", Payload.PRODUCTS_FOR_SEARCH)
    def test_user_can_add_product_to_the_cart(self, browser, product):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.find_product(product)
        product_page = ProductPage(browser, browser.current_url)
        product_page.order_the_product()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.verify_product_is_in_cart(product)
        cart_page.delete_product_from_the_cart()

