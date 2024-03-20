from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Product didn't added to the basket"
