import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.jd.com")

    @unittest.skip('since to click btn_rush')
    def test_find_btn_rush(self):
        btn_rush = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '秒杀')))
        assert '秒杀' in btn_rush.text

    def test_swith_to_miao_sha_window(self):
        btn_rush = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '秒杀')))
        btn_rush.click()
        try:
            self.driver.switch_to_window('&3AB9D23F7A4B3C9B=MGUP4QLMNNF5HRZQXGDW7CUOWZNDKX4SLQVOA3AQNFZ3GQKIKYENY5Q5UR6E7KSTSVJP4LQUPOAMC623X2UHEPLEPI')
        except Exception as ex:
            print(ex)
        finally:
            time.sleep(5)
            self.driver.switch_to_window('&3AB9D23F7A4B3C9B=MGUP4QLMNNF5HRZQXGDW7CUOWZNDKX4SLQVOA3AQNFZ3GQKIKYENY5Q5UR6E7KSTSVJP4LQUPOAMC623X2UHEPLEPI')

        for handler in self.driver.window_handles:
            print(handler)
        assert '京东秒杀-正品保证、天天低价、限时限量' in self.driver.title
    
    def tearDown(self):
        self.driver.close()
        

if (__name__ == '__main__'):
    unittest.main()
