import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://www.mercadolibre.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        
    def tearDown(self) -> None:
        self.driver.quit()

    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element(By.ID, 'CO')
        country.click()
        
        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        location.click()
        
        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        condition.click()
        
        order_menu = driver.find_element(By.CLASS_NAME, 'ui-dropdown__link')
        order_menu.click()
        
        higher_price = driver.find_element(By.CSS_SELECTOR, '#')
        higher_price.click()
        
        articles = []
        prices = []
        
        for i in range(5):
            article_name = driver.find_element(By.XPATH, f'//Buscar[{i + 1}]').text
            articles.append(article_name)
            
            article_price = driver.find_element(By.XPATH, '#PEndiente[{i+1}]').text
            prices.append(article_price)
            
        print(articles, prices)
            
            
if __name__ == '__main__':
    unittest.main(verbosity=2)