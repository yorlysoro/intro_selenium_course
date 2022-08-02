import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicContronls(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
        
    def tearDown(self) -> None:
        self.driver.quit()
    
    def test_dynamic_controls(self):
        check_box = self.driver.find_element(By.CSS_SELECTOR, '#checkbox')
        check_box.click()
        
        remove_button = self.driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_button.click()
        
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox')))
        remove_button.click()
        
        enable_disable_button = self.driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()
        
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        
        text_area = self.driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('platzi')
        
        enable_disable_button.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
