from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.calculator.net/')
elements_link = driver.find_elements(By.PARTIAL_LINK_TEXT,'Calculator')
cal_num = len(elements_link)
print(f'{cal_num}')

selenium_base.selenium_end(driver)