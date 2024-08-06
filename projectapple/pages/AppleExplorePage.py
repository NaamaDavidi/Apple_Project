from selenium.webdriver.common.by import By


class ExplorePage():

    def __init__(self,driver):
        self.driver = driver
        self.find_item_iphone = 'figure[class="chapternav-icon"]'



    def select_item_macbook(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'MacBook')
        click_item[0].click()

    def select_item_airpods(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'airpods')
        click_item[-2].click()


    def select_item_iphone(self):
        click_item = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'iphone')
        click_item[0].click()
        click_icon = self.driver.find_elements(By.CSS_SELECTOR,self.find_item_iphone)
        click_icon[0].click()