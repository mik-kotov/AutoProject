from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_product_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Product didn't added to the basket"

    def should_not_product_added_to_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_ADD_TO_BASKET), "Success message is presented, but should not be"

    def should_be_same_names_of_products_in_card_and_in_alert(self):
        assert (self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_THE_PRODUCT_CARD).text ==
                self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_THE_ALERT_OF_PRODUCT_ADDED).text), "Names are not same"

    def should_be_same_prices_in_cart_and_in_product_card(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text ==
                self.browser.find_element(*ProductPageLocators.BASKET_SUM_AFTER_PRODUCT_ADDED).text), "Prices are not same"

