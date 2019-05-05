# encoding = utf-8
from selenium import webdriver
from PageObject import Baidu_Main_Page_Plus
from time import sleep
import unittest
class Search_Page(unittest.TestCase):
    def setUp(self):
        self.chrome_driver = webdriver.Chrome()
        self.string = "davieyang"
    def test_search_davieyang(self):
        self.chrome_driver.get("http://www.baidu.com")
        self.baidu_main_page_plus = Baidu_Main_Page_Plus.Search_Page_Element(self.chrome_driver)
        try:
            self.baidu_main_page_plus.input_search_string(self.string)
            self.baidu_main_page_plus.button_search().click()
            sleep(3)  #  等待3秒
            self.assertTrue("davieyang" in self.chrome_driver.page_source)
        except AssertionError as e:
            raise e
    def tearDown(self):
        self.chrome_driver.quit()
if __name__ == '__main__':
    unittest.main()
