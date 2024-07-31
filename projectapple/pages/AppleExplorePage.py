from selenium.webdriver.common.by import By


class ExplorePage():

    def __init__(self,driver):
        self.driver = driver



    def select_item(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'MacBook')
        click_item[0].click()