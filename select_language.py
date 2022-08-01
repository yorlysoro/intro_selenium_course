import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://lookbook.altimawebsystems.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = [] 
        
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        self.assertEqual(3, len(select_language.options))
        
        for option in select_language.options:
            act_options.append(option.text)
        
        self.assertListEqual(exp_options, act_options)
        self.assertEqual('English', select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)
        
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        select_language.select_by_index(0)

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
