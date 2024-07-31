from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Python.selenium.selenium_base_example import selenuim_base_example

selenium_base = selenuim_base_example()

driver = selenium_base.selenium_start('https://demo.guru99.com/test/newtours/reservation.php')
sleep(5)
tripType = driver.find_elements(By.NAME,'tripType')
sleep(3)
tripType[1].click()
tripType[0].is_enabled()
tripType[1].is_selected()
sleep(3)
Passengers = Select(driver.find_element(By.NAME,'passCount'))
sleep(3)
Passengers.select_by_value('2')
sleep(3)
Departing_From = Select(driver.find_element(By.NAME,'fromPort'))
sleep(3)
Departing_From.select_by_value('Frankfurt')
On_mounth = Select(driver.find_element(By.NAME,'fromMonth'))
On_mounth.select_by_value('2')
on_day = Select(driver.find_element(By.NAME,'fromDay'))
on_day.select_by_value('6')
Arriving_In = Select(driver.find_element(By.NAME,'toPort'))
Arriving_In.select_by_value('London')
Returning_month = Select(driver.find_element(By.NAME,'toMonth'))
Returning_month.select_by_value('3')
Returning_day = Select(driver.find_element(By.NAME,'toDay'))
Returning_day.select_by_value('9')
Class = driver.find_elements(By.NAME,'servClass')
sleep(3)
Class[2].click()
Class[0].is_enabled()
Class[1].is_enabled()
Class[2].is_selected()
sleep(3)
airline = Select(driver.find_element(By.NAME,'airline'))
airline.select_by_visible_text('Blue Skies Airlines')
send_button = driver.find_element(By.NAME,'findFlights')
send_button.click()

