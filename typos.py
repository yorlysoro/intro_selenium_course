import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Typos').click()
        
    def tearDown(self) -> None:
        self.driver.quit()
    
    def test_typos(self):
        driver = self.driver
        
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            driver.refresh()
            
        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True
        
        self.assertEqual(found, True)
        
        print(f"It took {tries} tries to find the typo")


if __name__ == '__main__':
    unittest.main(verbosity=2)