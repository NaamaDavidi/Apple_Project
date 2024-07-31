import unittest

from selenium_page_object.pages.LoginPage import LoginPage
from selenium_page_object.pages.ProductPage import ProductPage
from selenium_page_object.tests.baseSelenium import baseSelenium
from selenium_page_object.tests.globals import url_base, user_text, password_text


class test_price_text(unittest.TestCase):

     def test_first_price_text(self):
        base = baseSelenium()


        driver = base.selenium_start(url_base)
        login_page= LoginPage(driver)
        product_page = ProductPage(driver)

        login_page.login_with_user_password(user_text,password_text)
        price_text = product_page.get_price()






        base.selenium_end(driver)