import time
import unittest

from selenium.webdriver.common.by import By

from projectapple.pages import Apple_home_page
from projectapple.pages.AppleBaseSelenium import ProjectBaseSelenium
from projectapple.pages.AppleGlobals import url_base
from projectapple.pages.AppleProductPage import Product_Page
from projectapple.pages.Apple_home_page import home_page
from projectapple.pages.AppleExplorePage import ExplorePage



class AppleTest(unittest.TestCase):

    def setUp(self):
        self.base = ProjectBaseSelenium()
        self.driver = self.base.selenium_start(url_base)



    def test_search(self):

        limit = 1400

        home_page_object = home_page(self.driver)
        explore_page = ExplorePage(self.driver)
        product_page = Product_Page(self.driver)

        home_page_object.create_search("macbook")
        time.sleep(3)
        explore_page.select_item()
        price = product_page.find_price_offer()
        assert price>limit  ,"the price is lower than 1400 not as expected"




    def tearDown(self):
        print ('into tear down')
        self.base.selenium_end(self.driver)

