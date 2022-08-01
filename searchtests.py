import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://lookbook.altimawebsystems.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        
    # def test_search_text_field(self):
    #     search_field = self.driver.find_element(By.ID, "search")

    def tearDown(self) -> None:
        self.driver.quit()
        
    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element(By.NAME, "q")

    # def test_search_text_field_by_class_name(self):
    #     search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    # def test_search_button_enabled(self):
    #     button = self.driver.find_element(By.CLASS_NAME, "button")

    # def test_count_of_promo_banner_images(self):
    #     banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
    #     banners = banner_list.find_element(By.TAG_NAME, "img")
    #     self.assertEqual(3, len(banners))
    
    # def test_vip_promo(self):
    #     vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
        
    # def test_shopping_cart(self):
    #     shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')

    def test_search_tee(self):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()
        
        search_field.send_keys('tee')
        search_field.submit()
        
    def test_search_salt_shaker(self):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys('salt shaker')
        search_field.submit()
        
        products = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li[1]/div/h2/a')
        self.assertEqual(1, len(products))

     
if __name__ == '__main__':
    unittest.main(verbosity=2)
