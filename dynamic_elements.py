import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddRemoveElements(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
        
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_name_elements(self):
        options = []
        menu = 5
        tries = 1
        
        while len(options) < 5:
            options.clear()
            for i in range(menu):
                try:
                    option_name = self.driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option Number {i + 1}  is not found")
                    tries += 1
                    self.driver.refresh()
        print(f"Finished in {tries} tries")
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
