from encodings import search_function
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LanguageOptions(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def tearDown(self) -> None:
        self.driver.quit()
    
    def test_browser_navigation(self):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()
        
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
