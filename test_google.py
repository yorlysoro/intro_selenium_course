import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from google_page import GooglePage


class GoogleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="chromedriver")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('platzi')
        
        self.assertEqual('platzi', google.keyword)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
