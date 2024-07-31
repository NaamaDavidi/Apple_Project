from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.demoblaze.com/')
contact_page = driver.find_element(By.PARTIAL_LINK_TEXT,'Contact')
contact_page_text = contact_page.text
print(f'text found the value is {contact_page_text}')


if contact_page_text =='Contact':
    print(f'text is identical to Contact')
    contact_page.click()

else:
    print("Link text isn't identical to Contact")
