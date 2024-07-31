from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://advantageonlineshopping.com/#/')
sleep(5)
contact_us = driver.find_element(By.LINK_TEXT,'CONTACT US')
contact_us.click()
sleep(5)
select_category = Select(driver.find_element(By.NAME,'categoryListboxContactUs'))
select_category.select_by_value('object:60')
sleep(5)
select_product = Select(driver.find_element(By.NAME,'productListboxContactUs'))
select_product.select_by_value('object:133')
sleep(5)
email = driver.find_element(By.NAME,'emailContactUs')
email.send_keys('naamadavidi6468@gmail.com')
sleep(5)
input_box = driver.find_element(By.NAME,'subjectTextareaContactUs')
input_box.send_keys('bhbhhbhbhbhbhbh')
sleep(3)
send = driver.find_element(By.ID,'send_btn')
