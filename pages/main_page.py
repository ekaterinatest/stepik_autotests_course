import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
	def go_to_login_page(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
		login_link.click()

	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"