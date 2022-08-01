from encodings import search_function
from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://lookbook.altimawebsystems.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
        
        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()
        
        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        
        alert.accept()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
