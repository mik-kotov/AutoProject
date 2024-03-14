
import time
from selenium.webdriver.common.by import By



def test_spanish_button_add_to_basket(browser):
    time.sleep(5)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

