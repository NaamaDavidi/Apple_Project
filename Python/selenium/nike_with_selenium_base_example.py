from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.nike.com')


driver.find_element(By.LINK_TEXT,'Men')


selenium_base.selenium_end(driver)