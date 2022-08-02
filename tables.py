from email import header
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tables(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
        
    def tearDown(self) -> None:
        self.driver.quit()
    
    def test_sort_tables(self):
        driver = self.driver
        
        table_data = [[] for i in range(5)]
        print(table_data)
        
        for i in range(5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)
            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{j+1}]')
                table_data[i].append(row_data.text)
        print(table_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)