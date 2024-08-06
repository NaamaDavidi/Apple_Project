import time
import unittest

from selenium.webdriver.common.by import By

from projectapple.pages import Apple_home_page
from projectapple.pages.AppleBaseSelenium import ProjectBaseSelenium
from projectapple.pages.AppleGlobals import url_base, limit1, limit2
from projectapple.pages.AppleProductPage import Product_Page
from projectapple.pages.Apple_home_page import home_page
from projectapple.pages.AppleExplorePage import ExplorePage



class AppleTest(unittest.TestCase):

    def setUp(self):
        self.base = ProjectBaseSelenium()
        self.driver = self.base.selenium_start(url_base)
        self.home_page_object = home_page(self.driver)
        self.explore_page = ExplorePage(self.driver)
        self.product_page = Product_Page(self.driver)


    def test_search_macbook(self):
        self.home_page_object.create_search("macbook")
        time.sleep(3)
        self.explore_page.select_item_macbook()
        price = self.product_page.find_price_offer_macbook()
        assert price>limit1,"the price is lower than 1400 not as expected"


    def test_search_airpods(self):
        self.home_page_object.create_search("airpods")
        time.sleep(3)
        self.explore_page.select_item_airpods()
        price = self.product_page.find_price_offer_airpods()
        assert price < limit2, "the price is higher than 150 not as expected"


    def test_search_iphone(self):
        self.home_page_object.create_search("iphone")
        time.sleep(3)
        self.explore_page.select_item_iphone()
        price = self.product_page.find_price_offer_iphone()
        assert price < limit1, "the price is cheaper than first item"


    def tearDown(self):
        print ('into tear down')
        self.base.selenium_end(self.driver)

