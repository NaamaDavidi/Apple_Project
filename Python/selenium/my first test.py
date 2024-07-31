from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# driver.get('https://www.google.com')
# search = driver.find_element(By.ID,'APjFqb')
# search.click()
# search.click()
# search.send_keys('cat')
# search.send_keys(Keys.ENTER)
# driver.close()
# print('test end')

driver.get('https://www.saucedemo.com')
username = driver.find_element(By.ID,'user-name')
username.click()
username.send_keys('standard_user')
password = driver.find_element(By.ID,'password')
password.click()
password.send_keys('secret_sauce')
login_key = driver.find_element(By.ID,'login-button')
login_key.click()
price = driver.find_element(By.CLASS_NAME,'inventory_item_price')
price_text = price.text
print(f'price found the value is {price_text}')





driver.close()
print('test end')