import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projectapple.pages.AppleGlobals import item1, item2, item3


class ExplorePage():

    def __init__(self,driver):
        self.driver = driver
        self.find_item_iphone = 'li[class="chapternav-item chapternav-item-iphone-15-pro"]'



    def select_item_macbook(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,item1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(click_item[0]))
        click_item[0].click()

    def select_item_airpods(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,item2)
        click_item[-2].click()


    def select_item_iphone(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,item3)
        click_item[0].click()
        time.sleep(5)
        click_icon = self.driver.find_element(By.CSS_SELECTOR,self.find_item_iphone)
        click_icon.click()