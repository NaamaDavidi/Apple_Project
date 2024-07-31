import time

from selenium.webdriver.common.by import By

from selenium_page_object.tests.globals import password_text, user_text


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.user = 'user-name'
        self.password = 'password'
        self.login = 'login-button'

    def set_user(self,user_text):
        user_element = self.driver.find_element(By.ID,self.user)
        user_element.click()
        user_element.clear()
        user_element.send_keys(user_text)
        user_element.click()



    def set_password(self,password_text):
        password_element = self.driver.find_element(By.ID,self.password)
        password_element.click()
        password_element.clear()
        password_element.send_keys(password_text)

    def click_login(self):
        login_button = self.driver.find_element(By.ID,self.login)
        login_button.click()

    def login_with_user_password(self,user_text,password_text):
        print(f'try to login with user {user_text} and password {password_text}')
        self.set_user(user_text)
        self.set_password(password_text)
        self.click_login()
        time.sleep(3)