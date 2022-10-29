from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    MESSAGE_CART_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
