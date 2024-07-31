from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.calculator.net/"

driver.get(url)
bmi_button = driver.find_element(By.PARTIAL_LINK_TEXT, "BMI")

bmi_button.click()
sleep(3)
calorie_button = driver.find_element(By.LINK_TEXT, "Calorie")
calorie_text = calorie_button.text
print(calorie_text)




driver.close()
print("test end")