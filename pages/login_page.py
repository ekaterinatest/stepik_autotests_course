from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert 'login' in current_url, "Current URL is not login URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
