# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = None
class Browser_Controller:

    def __init__(self, driver=''):
        self.driver = driver


    def driver_browser(self, browser_type, base_url):
        if browser_type.lower() == "firefox":  # 如果参数转换成小写后是firefox则启动火狐浏览器
            driver = webdriver.Firefox()
        elif browser_type.lower() == "chrome":  # 如果参数转换成小写后是chrome则启动谷歌浏览器
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Ie()  # 如果参数不是上边两种之一，则启动IE浏览器
        driver.get(base_url)  # 驱动浏览器打开self.base_url
        driver.maximize_window()  # 最大化
        driver.implicitly_wait(10)  # 全局等待
        return driver  # 返回浏览器驱动

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def set_browser_window(self, weight, high):
        """
        设置浏览器窗口宽和高
        :param driver:
        :param weight:
        :param high:
        :return:
        """
        self.driver.set_window_size(weight, high)

    def switch_to_iframe(self, frame):
        """
        用于切换进页面的iframe控件
        :param iframe:
        :return:
        """
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        从iframe中切换回主页页面
        :return:
        """
        self.driver.switch_to.default_content()

    def switch_to_alert(self):
        """
        切换进alert控件
        :return:
        """
        pop_dailog = self.driver.switch_to.alert
        return pop_dailog

    def select_by_index(self, element, index):
        """
        通过下拉菜单的索引，完成对选项的选择
        :param element:
        :param value:
        :return:
        """
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        """
        通过选项值，完成对选项的选择
        :param element:
        :param value:
        :return:
        """
        Select(element).select_by_value(value)

    def select_by_text(self, element, text):
        """
        通过选项的文本，完成对选项的选择
        :param element:
        :param text:
        :return:
        """
        Select(element).select_by_visible_text(text)
