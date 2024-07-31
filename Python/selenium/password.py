from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://www.calculator.net/password-generator.html')
# password_length = driver.find_element(By.NAME,'lennumber')
# password_length.clear()
# sleep(3)
# password_length.send_keys(15)
check_box = driver.find_elements(By.CLASS_NAME,'cbcontainer')
check_box[1].is_enabled()
check_box[2].is_selected()
check_box[3].is_enabled()
check_box[4].is_selected()

submit_button = driver.find_element(By.NAME,'submit1')
submit_button.click()
result = driver.find_element(By.ID,'resultid')
password = result.text
start_index = password.index('Password')+8
stop_index = password.index('Password Strength')-1
final = password[start_index:stop_index]
final = final.strip()
print(f'the result is {final}')
selenium_base.selenium_end()