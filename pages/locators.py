from selenium.webdriver.common.by import By

class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group :nth-child(1)")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():

    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-info")
    BOOK_NAME_IN_THE_PRODUCT_CARD = (By.CSS_SELECTOR, ".product_main > :nth-child(1)")
    BOOK_NAME_IN_THE_ALERT_OF_PRODUCT_ADDED = (By.CSS_SELECTOR,"#messages :nth-child(1) > .alertinner :nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_SUM_AFTER_PRODUCT_ADDED = (By.CSS_SELECTOR, ".alertinner > p:nth-child(1) > :nth-child(1)")

class BasketPageLocators():

    SOME_PRODUCTS_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")


