from .pages.product_page import ProductPage
import math
import time
import pytest
from selenium.common.exceptions import NoAlertPresentException
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from .pages.base_page import BasePage

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

# def test_guest_can_add_product_to_basket(browser):
#     link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()

def test_names_of_products_in_card_and_in_alert_are_same(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        solve_quiz_and_get_code(page)
        page.should_be_same_names_of_products_in_card_and_in_alert()


def test_price_of_product_in_card_and_cost_of_basket_are_same(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    solve_quiz_and_get_code(page)
    page.should_be_same_prices_in_cart_and_in_product_card()

@pytest.mark.parametrize('number', ["1","2","3","4","5","6","8", "9",
                                    pytest.param("7", marks=pytest.mark.xfail(reason="some bug"))])
def test_searching_for_bad_number_in_promo_link(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    solve_quiz_and_get_code(page)
    page.should_be_same_prices_in_cart_and_in_product_card()
    page.should_be_same_names_of_products_in_card_and_in_alert()


def test_product_added_to_basket_message_when_open_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_product_added_to_basket_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Success message is presented, but should not be"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ALERT_ADD_TO_BASKET), "Success message is presented, but should not be"

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_the_basket()
    assert page.is_not_element_present(
        *BasketPageLocators.SOME_PRODUCTS_IN_THE_BASKET), "The basket should be empty"