# encoding = utf-8
import unittest
from Util.BrowserController import Browser_Controller
from Util.Keyboard_Simulation import Simulate_Keyboard
from Util.Clipboard_Simulation import Simulate_Clipboard
from Util.Mouse_Simulation import Simulate_Mouse
from selenium import webdriver
import time
from Util.Intelligent_Wait import WaitUntil
from selenium.webdriver.common.action_chains import ActionChains
from Util import GetLog

testlogger = GetLog.Logger('Test_Advanced_Application').getlog()  # 调用封装好的方法


class Test_Advanced_Application(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.baidu.com'  # 定义url
    def test_control_browser(self):
        BC = Browser_Controller()  # 实例化Browser_Controller类
        chrome_driver = BC.driver_browser("chrome", self.url)  # 调用start_browser方法用于启动相应浏览器并打开url
        Browser_Controller(chrome_driver).set_browser_window(400, 800)
        chrome_driver.find_element_by_id("kw").send_keys("__davieyang__")
        chrome_driver.find_element_by_id("su").click()
        firefox_driver = BC.driver_browser("firefox", self.url)
        firefox_driver.find_element_by_id("kw").send_keys("__davieyang__")
        firefox_driver.find_element_by_id("su").click()
        ie_driver = BC.driver_browser("ie", self.url)  # 调用start_browser方法用于启动相应浏览器并打开url
        ie_driver.find_element_by_id("kw").send_keys("__davieyang__")
        ie_driver.find_element_by_id("su").click()

    def test_simulate_keyboard(self):

        Simulate_Keyboard.click_onekey('enter')
        Simulate_Keyboard.click_twokey('ctrl', 'c')
        Simulate_Keyboard.click_onekey('enter')

    def test_simulate_clipboard(self):
        Simulate_Clipboard.set_clipboard("set clipboard")
        str = Simulate_Clipboard.get_clipboard()
        print(str)

    def test_simulate_mouse(self):
        chr_driver = webdriver.Chrome()
        chr_driver.get(self.url)
        element = chr_driver.find_element_by_link_text("设置")
        Simulate_Mouse(chr_driver).move_mouse(element)
        time.sleep(5)

    def test_wait(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://mail.126.com")
        # 实例化WaitUntil类
        wait_until = WaitUntil(driver)
        # 判断如果iframe存在则切换进去
        wait_until.frame_to_be_available_and_switch_to_it\
            ("xpath", "html/body/div[2]/div/div/div[3]/div[3]/div[1]/div[1]/iframe")
        # 等待页面元素xpath = //input[@name='email']的出现
        wait_until.visibility_element_located("xpath", "//input[@name='email']")
        # 显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        wait_until.presence_of_element_located("xpath", "//input[@name='email']")
        driver.quit()

    def test_switch_iframe(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("https://mail.163.com")
        time.sleep(10)
        frame = chrome_driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")
        Browser_Controller(chrome_driver).switch_to_iframe(frame)
        time.sleep(5)
        chrome_driver.find_element_by_name("email").send_keys("15901281916")
        chrome_driver.find_element_by_name("password").send_keys("Ethan005!@#")
        chrome_driver.find_element_by_id("dologin").click()

    def test_switch_to_alert(self):
        chrome_driver = webdriver.Chrome()
        # 浏览器打开我们刚才新建的html文件
        chrome_driver.get("file:///C:/Users/davieyang/Desktop/test_alert.html")
        time.sleep(3)
        #  点击alert按钮
        chrome_driver.find_element_by_id("alert").click()
        time.sleep(10)
        #  调用我们封装好的方法
        al = Browser_Controller(chrome_driver).switch_to_alert()
        print(al.text)  #  打印弹窗中的文本
        # 相当于点击弹窗中的确定按钮，但实际并不是点击只是弹窗对象提供的方法，效果一样
        al.accept()

    def test_switch_to_confirm(self):
        chrome_driver = webdriver.Chrome()
        # 浏览器打开我们刚才新建的html文件
        chrome_driver.get("file:///C:/Users/davieyang/Desktop/test_alert.html")
        time.sleep(3)
        #  点击alert按钮
        chrome_driver.find_element_by_id("confirm").click()
        time.sleep(3)
        #  调用我们封装好的方法
        al = Browser_Controller(chrome_driver).switch_to_alert()
        print(al.text)  #  打印弹窗中的文本
        # 相当于点击弹窗中的确定按钮，但实际并不是点击只是弹窗对象提供的方法，效果一样
        al.dismiss()

    def test_switch_to_prompt(self):
        chrome_driver = webdriver.Chrome()
        # 浏览器打开我们刚才新建的html文件
        chrome_driver.get("file:///C:/Users/davieyang/Desktop/test_alert.html")
        time.sleep(3)
        #  点击alert按钮
        chrome_driver.find_element_by_id("prompt").click()
        time.sleep(3)
        #  调用我们封装好的方法
        al = Browser_Controller(chrome_driver).switch_to_alert()
        print(al.text)  #  打印弹窗中的文本
        # 相当于点击弹窗中的确定按钮，但实际并不是点击只是弹窗对象提供的方法，效果一样
        al.accept()

    def test_select(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("http://www.baidu.com")
        chrome_driver.implicitly_wait(30)
        mouse = chrome_driver.find_element_by_link_text("设置")
        ActionChains(chrome_driver).move_to_element(mouse).perform()
        chrome_driver.find_element_by_link_text("搜索设置").click()
        time.sleep(5)
        chrome_driver.find_element_by_name("NR").click()
        time.sleep(5)
        select = chrome_driver.find_element_by_name("NR")
        Browser_Controller(chrome_driver).select_by_value(select, "20")
        time.sleep(5)
        Browser_Controller(chrome_driver).select_by_index(select, 1)
        time.sleep(5)
        Browser_Controller(chrome_driver).select_by_text(select, "每页显示50条")
        time.sleep(5)

    def test_get_log(self):
        testlogger.info("打开浏览器")
        driver = webdriver.Chrome()
        driver.maximize_window()
        testlogger.info("最大化浏览器窗口。")
        driver.implicitly_wait(10)
        testlogger.info("打开百度首页。")
        driver.get("https://www.baidu.com")
        testlogger.info("暂停3秒。")
        time.sleep(3)
        testlogger.info("关闭并退出浏览器")
        driver.quit()

        with self.assertLogs(testlogger, level=20) as log:
            testlogger.error("打开浏览器")
            testlogger.info('关闭并退出浏览器')
            self.assertEqual(log.output,
                             ['ERROR:Test_Advanced_Application:打开浏览器',
                              'INFO:Test_Advanced_Application:关闭并退出浏览器']
                             )


if __name__ == '__main__':
    unittest.main(verbosity=2)
