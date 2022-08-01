import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddRemoveElements(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_add_remove(self):
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        
        total_elements = elements_added + elements_removed
        
        add_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        
        for i in range(elements_added):
            add_button.click()
        
        for i in range(elements_removed):
            try:
                delete_button = self.driver.find_element(By.XPATH, '//*[@id="elements"]/button[3]')
                delete_button.click()
            except:
                print("You're trying to delete more elements the existing")
                break
        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print("There 0 are elements on screen")


if __name__ == '__main__':
    unittest.main(verbosity=2)