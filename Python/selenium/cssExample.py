from selenium.webdriver.common.by import By

from Python.selenium.selenium_base_example import selenuim_base_example


class cssExample():
    base = selenuim_base_example()
    driver = base.selenium_start('https://www.saucedemo.com/')
    user = driver.find_element(By.CSS_SELECTOR,"input[class='input_error form_input']")
    user.click()
    user.send_keys('standard_user')
    pw = driver.find_element(By.CSS_SELECTOR,"input[data-test='password']")
    pw.click()
    pw.send_keys('secret_sauce')
    login = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
    login.click()


    base.selenium_end(driver)