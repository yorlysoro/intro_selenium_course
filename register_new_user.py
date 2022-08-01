import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://lookbook.altimawebsystems.com/')
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

    def test_new_user(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[2]/div/a/span[2]')
        self.driver.find_element(By.LINK_TEXT, 'Log In').click()
        
        create_account_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[2]/div/a/span[2]')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        
        self.assertEqual('Create New Customer Account', self.driver.title)
        first_name = self.driver.find_element(By.ID, 'first_name')
        self.driver.implicitly_wait(1)
        middle_name = self.driver.find_element(By.ID, ' middle_name')
        self.driver.implicitly_wait(1)
        last_name = self.driver.find_element(By.ID, ' last_name')
        self.driver.implicitly_wait(1)
        email_address = self.driver.find_element(By.ID, ' email_address')
        self.driver.implicitly_wait(1)
        news_letter_subscription = self.driver.find_element(By.ID, 'is_subscribed')
        self.driver.implicitly_wait(1)
        password = self.driver.find_element(By.ID, 'password')
        self.driver.implicitly_wait(1)
        confirm_password = self.driver.find_element(By.ID, 'confirm_password')
        self.driver.implicitly_wait(1)
        submit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[2]/div/a/span[2]')
        
        self.assertTrue(first_name.is_enabled() and 
                        last_name.is_enabled() and 
                        middle_name.is_enabled() and 
                        email_address.is_enabled() and 
                        news_letter_subscription.is_enabled() and 
                        password.is_enabled() and 
                        confirm_password.is_enabled() and 
                        submit_button.is_enabled())

        first_name.send_keys('Test')
        last_name.send_keys('Test')
        middle_name.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()
