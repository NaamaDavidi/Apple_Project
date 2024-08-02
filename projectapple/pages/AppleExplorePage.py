from selenium.webdriver.common.by import By


class ExplorePage():

    def __init__(self,driver):
        self.driver = driver



    def select_item_macbook(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'MacBook')
        click_item[0].click()

    def select_item_airpods(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'airpods')
        click_item[-2].click()