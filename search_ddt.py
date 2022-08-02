import csv, unittest
from email import message
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data(file_name):
    rows = []
    data_file = open(file=file_name, mode='r', encoding='UTF-8')
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


@ddt
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
        
    
    @data(*get_data('testdata.csv'))
    @unpack
    
    def test_search_ddt(self, search_value, expected_count):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()
        
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = self.driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        
        expected_count = int(expected_count)
        
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = self.driver.find_element(By.CLASS_NAME, 'note-msg')
            self.assertEqual('Your search returns no results.', message)
        
        print(f'Found {len(products)} products')

     
if __name__ == '__main__':
    unittest.main(verbosity=2)
