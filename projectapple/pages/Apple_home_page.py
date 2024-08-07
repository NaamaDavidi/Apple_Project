import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class home_page():

    def __init__(self,driver):
        self.driver = driver
        self.search_icon = 'globalnav-menubutton-link-search'
        self.search_box = "input[class='globalnav-searchfield-input']"





    def create_search(self,search_text):
        search_icon = self.driver.find_element(By.ID, self.search_icon)
        search_icon.click()
        search_box = self.driver.find_element(By.CSS_SELECTOR,self.search_box)
        time.sleep(3)
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.ENTER)
