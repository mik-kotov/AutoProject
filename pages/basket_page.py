from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_the_basket_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.SOME_PRODUCTS_IN_THE_BASKET), "The basket should be empty"
    def should_be_only_message_of_basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRICE_OF_ITEM_IN_THE_BASKET), "There is no only text about basket is empty"