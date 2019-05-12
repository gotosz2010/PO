# 用于定义整个框架中所需要的全局常量值
# encoding = utf-8
"""
__title__ = ''
__author__ = 'davieyang'
__mtime__ = '2018/4/21'
"""
import os

# 获取当前文件所在目录的父目录的绝对路径
parent_directory_path = os.path.abspath('..')
print(parent_directory_path)

# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parent_directory_path + u"\\Configurations\\PageElementLocator.ini"
# 获取xml测试数据文件所在路径
xmldata = parent_directory_path + u"\\TestData\\test_search_data.xml"