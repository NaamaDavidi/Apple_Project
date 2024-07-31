from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
buttons = driver.find_elements(By.CLASS_NAME,'btn.btn-primary.btn-lg')
# bank_manager_text = bank_manager.text
# print(f'text found the value is {bank_manager_text}')
# bank_manager.click()
buttons[1].click()