from .pages.product_page import ProductPage
import math
import time
import pytest
from selenium.common.exceptions import NoAlertPresentException
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