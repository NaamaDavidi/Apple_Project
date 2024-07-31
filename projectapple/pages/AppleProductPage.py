import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Product_Page():

    def __init__(self,driver):
        self.driver = driver
        self.price_offer = 'all-access-pass__container'



    def find_price_offer(self):
        time.sleep(3)
        Price_Offer = self.driver.find_element(By.CSS_SELECTOR,"p[class= 'welcome__lockup-primary-copy has-dynamic-content']")
        price_Offer_text = Price_Offer.text
        print(f'price found the value is {price_Offer_text}')
        price_as_str = price_Offer_text
        index1=price_as_str.index("or")-1
        index2 = price_as_str.index("$")+1
        price_temp = price_as_str[index2:index1]
        time.sleep(3)
        print(price_temp)
        price = int(price_temp)
        return price
