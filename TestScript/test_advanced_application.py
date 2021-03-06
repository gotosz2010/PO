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
import os
from Util.JSAssistance import JS_Assistance
from Util.ParseMysql import Parse_Mysql
from TestData import SQL_Script

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
        wait_until.frame_to_be_available_and_switch_to_it \
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
        print(al.text)  # 打印弹窗中的文本
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
        print(al.text)  # 打印弹窗中的文本
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
        print(al.text)  # 打印弹窗中的文本
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

    def test_upload_by_sendkeys(self):
        chrome_driver = webdriver.Chrome()
        str = "E://test_upload_file.txt"
        chrome_driver.get("file:///C:/Users/Administrator/Desktop/fileupload.html")
        chrome_driver.find_element_by_name("fileupload").send_keys(str)
        time.sleep(10)
        chrome_driver.quit()

    def test_upload_by_autoit(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("file:///C:/Users/Administrator/Desktop/fileupload.html")
        chrome_driver.find_element_by_name("fileupload").click()
        os.system("E:\\PO\\Util\\upload_file.exe")
        time.sleep(10)
        chrome_driver.quit()

    def test_upload_by_simulation(self):
        Simulate_Clipboard.set_clipboard("E:\\test_upload_file.txt")
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("file:///C:/Users/Administrator/Desktop/fileupload.html")
        chrome_driver.find_element_by_name("fileupload").click()
        time.sleep(5)
        Simulate_Keyboard.click_twokey('ctrl', 'v')
        time.sleep(5)
        Simulate_Keyboard.click_onekey('enter')
        time.sleep(20)

    def test_cookies(self):
        cookie_dict = {'name': 'name_yang', 'value': 'cookie_yang'}
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("https://www.baidu.com")
        time.sleep(10)
        current_cookie = Browser_Controller(chrome_driver).get_current_cookies()
        print(current_cookie)
        Browser_Controller(chrome_driver).add_key_value_to_cookie(cookie_dict)
        key_cookie = Browser_Controller(chrome_driver).get_current_cookie_value('name_yang')
        print(key_cookie)
        Browser_Controller(chrome_driver).delete_current_cookie()
        current_cookie_2 = Browser_Controller(chrome_driver).get_current_cookies()
        print(str(current_cookie_2) + "只有这几个字没有cookie了")

    def test_js(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("http://www.baidu.com")
        chrome_driver.find_element_by_id("kw").send_keys("davieyang")
        chrome_driver.find_element_by_id("su").click()
        JS_Assistance(chrome_driver).scroll_to_bottom()
        time.sleep(3)
        JS_Assistance(chrome_driver).scroll_to_top()
        time.sleep(3)
        JS_Assistance(chrome_driver).scroll_to_bottom_page()
        time.sleep(3)
        JS_Assistance(chrome_driver).scrolltotop()
        time.sleep(3)
        JS_Assistance(chrome_driver).scrolltobottom()
        time.sleep(3)
        element = chrome_driver.find_element_by_xpath("//*[@id='help']/a[3]")
        JS_Assistance(chrome_driver).single_click(element)
        time.sleep(3)

    def test_table_util(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("file:///C:/Users/Administrator/Desktop/table.html")
        chrome_driver.implicitly_wait(20)
        table_element = chrome_driver.find_element_by_id("table")
        string = u"用例一失败"
        Browser_Controller(chrome_driver).click_element_in_table(table_element, string)

    def test_switch_window_handle(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get("http://www.baidu.com")
        baidu_main_handle = chrome_driver.current_window_handle
        print(baidu_main_handle)
        time.sleep(5)
        chrome_driver.find_element_by_link_text("登录").click()
        time.sleep(5)
        chrome_driver.find_element_by_link_text("立即注册").click()
        all_handles = chrome_driver.window_handles
        print(all_handles)
        for handle in all_handles:
            try:
                if handle != baidu_main_handle:
                    chrome_driver.switch_to.window(handle)
                    print("进入新窗口....")
                    chrome_driver.switch_to.window(baidu_main_handle)
                    chrome_driver.refresh()
                    chrome_driver.find_element_by_id("kw").send_keys("__davieyang__")
                    time.sleep(5)
                    chrome_driver.find_element_by_id("su").click()
                    time.sleep(5)
            except Exception as e:
                raise e
        chrome_driver.quit()

    def test_create_database(self):
        db = Parse_Mysql(
            host="localhost",
            port=3306,
            dbName="mysql",
            username="root",
            password="",
            charset="utf8"
            )
        createdatabase = SQL_Script.createdatabase
        db.create_database(createdatabase)

    def test_create_table(self):
        db = Parse_Mysql(
            host="localhost",
            port=3306,
            dbName="mysql",
            username="root",
            password="",
            charset="utf8"
            )
        createtable = SQL_Script.createtable
        db.create_table("automation", createtable)

    def test_insert_data(self):
        db = Parse_Mysql(
            host="localhost",
            port=3306,
            dbName="mysql",
            username="root",
            password="",
            charset="utf8"
            )
        data = SQL_Script.datalist
        insertdata = SQL_Script.insertdata
        db.insert_data("automation", insertdata, data)

    def test_get_data(self):
        db = Parse_Mysql(
            host="localhost",
            port=3306,
            dbName="mysql",
            username="root",
            password="",
            charset="utf8"
            )
        selectdata = SQL_Script.selectdata
        data = db.select_data_from_table("automation", selectdata)
        print(data)


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Test_Advanced_Application('test_create_database'))
    unittest.TextTestRunner().run(testunit)
