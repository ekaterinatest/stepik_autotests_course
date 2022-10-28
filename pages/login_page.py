from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in current_url, f"No login substring in the {current_url}"

        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True