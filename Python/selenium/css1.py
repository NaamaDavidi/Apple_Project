from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example


class css1():
    base = selenuim_base_example()
    driver = base.selenium_start('https://demo.applitools.com/app.html')
    search = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Start typing to search...']")
    search.click()
    search.send_keys('Starbucks coffee')
    