import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.calculator.net/')
bmi_button = driver.find_element(By.PARTIAL_LINK_TEXT,'BMI')
bmi_button.click()
time.sleep(3)
calorie_button = driver.find_element(By.PARTIAL_LINK_TEXT,'Calorie')
calorie_text = calorie_button.text
print(calorie_text)
calorie_button.click()


driver.close()
print('test end')