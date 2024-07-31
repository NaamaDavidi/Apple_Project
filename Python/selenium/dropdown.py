from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.saucedemo.com')
username = driver.find_element(By.ID,'user-name')
username.click()
username.send_keys('standard_user')
password = driver.find_element(By.ID,'password')
password.click()
password.send_keys('secret_sauce')
login_key = driver.find_element(By.ID,'login-button')
login_key.click()

sort_drop_down = Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
sort_drop_down.select_by_index(3)
sleep(3)
sort_drop_down.select_by_value('az')
sleep(3)
sort_drop_down.select_by_visible_text('Price (low to high)')
sleep(3)

selenium_base.selenium_end(driver)
print('test end')