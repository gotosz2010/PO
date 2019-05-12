import unittest
import os
from Util.BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # 获取当前文件所在目录的父目录的绝对路径
    parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_suite = unittest.defaultTestLoader.discover('TestScript', pattern='test*.py')  # 定义测试集合
    result = BeautifulReport(test_suite)  # 将测试集合穿给BeautifulReport
    result.report(filename='测试报告', description='测试报告'
                  , log_path=parentDirPath + "\\TestResult\\")  # 调用report方法并传参生成报告
