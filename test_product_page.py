from .pages.product_page import ProductPage
import time
def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_product_to_basket()
    time.sleep(3)
    page.should_product_added_to_basket()
