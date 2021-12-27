from appium.webdriver.common.appiumby import AppiumBy as By
# from selenium.webdriver.common.by import By


class BasePageLocators:
    def __init__(self, *args, **kwargs):
        super(BasePageLocators, self).__init__(*args, **kwargs)


class MainPageLocators(BasePageLocators):
    LOGO = (By.XPATH, "//*[@id='container']//header/div[3]//a/img")
    CART_BUTTON = (By.XPATH, "//*[@id='cart-desktop']")


    DROP_DOWN_MENU_BUTTON = (By.XPATH, "//*[@id='navigation-sidebar']/div[2]/a")
    CART_MOBILE_BUTTON = (By.XPATH, "//*[@id='cart-mobile']/a")

    PRODUCT_FAST_SEARCH_INPUT = (By.XPATH, "*//input[1]")
    IFRAME = (By.XPATH, "//*[@id='fast-search-modal']/div/div/iframe")

    PRODUCT_LINK_XPATH_PATTERN = "//a[contains(text(), '{product}')]"

    @classmethod
    def get_product_link_locator(cls, product):
        return By.XPATH, cls.PRODUCT_LINK_XPATH_PATTERN.format(product=product)


class ProductPageLocators(BasePageLocators):
    PRODUCT_TITLE = (By.XPATH, "//h1[@class='catalog-masthead__title']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='container']//main//aside//a[3]")
    GO_TO_CART_BUTTON = (By.XPATH, "//div[@id='cart-desktop']/a[@class='b-top-profile__cart']")
    CLOSE_IFRAME_BUTTON = (By.XPATH, "//*[@class='product-recommended__sidebar-close']")


class CartPageLocators(BasePageLocators):
    PRODUCT_LINK_SELECTOR_PATTERN = "//*[(contains(text(), '{product}'))]"

    @classmethod
    def get_product_locator(cls, product):
        return By.XPATH, cls.PRODUCT_LINK_SELECTOR_PATTERN.format(product=product)

    REMOVE_BUTTON = (By.XPATH, '//*[contains(@class, "button_remove")]')
    INCREMENT_PRODUCT_BUTTON = (By.XPATH, "//a[contains(@class, 'cart-form__button_increment')]")
