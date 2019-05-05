# encoding = utf-8
from selenium import webdriver
from PageObject import Baidu_Main_Page
from time import sleep
import unittest
class Search_Page(unittest.TestCase):
    def setUp(self):
        self.chrome_driver = webdriver.Chrome()
        self.string = "davieyang"
    def test_search_davieyang(self):
        try:
            Baidu_Main_Page.search_string(self.chrome_driver, self.string)  # 调用前面封装好的search_string方法
            sleep(3)  #  等待3秒
            self.assertTrue("davieyang" in self.chrome_driver.page_source)
        except AssertionError as e:
            raise e
    def tearDown(self):
        self.chrome_driver.quit()
if __name__ == '__main__':
    unittest.main()
