from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "login" in self.browser.current_url, "Text 'login' didn't found in the URL"

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, browser, email, password):
        self.go_to_login_page()
        email_input_window = browser.find_element(*LoginPageLocators.REGISTER_WINDOW_OF_EMAIL_INPUT)
        email_input_window.send_keys(email)
        first_password_input_window = browser.find_element(*LoginPageLocators.REGISTER_WINDOW_OF_PASSWORD_INPUT)
        first_password_input_window.send_keys(password)
        second_password_input_window = browser.find_element(*LoginPageLocators.REGISTER_WINDOW_OF_PASSWORD_SECOND_INPUT)
        second_password_input_window.send_keys(password)
        registration_submit_button = browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        registration_submit_button.click()

