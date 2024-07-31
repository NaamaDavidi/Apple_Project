import time

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print('test start')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.ebay.com')
search = driver.find_element(By.ID,'gh-ac')
time.sleep(3)
search.click()
search.clear()
search.send_keys('mans shoes')
search.send_keys(Keys.ENTER)
print('test end')