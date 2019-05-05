# encoding = utf-8
from Util import HTMLTestRunner
import unittest
import time
import os

class StartTest(object):

    def __init__(self):
        print("generate test reports...")

    @staticmethod
    def starttest():
        # 获取当前文件所在目录的父目录的绝对路径
        parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(parentDirPath)
        test_suite = unittest.defaultTestLoader.discover('TestScript', pattern='test*.py')
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filename = parentDirPath + "\\PO\\TestResult\\Results-" + current_time + "result.html"
        print(filename)
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner\
            (stream=fp, title='Result', description='Test_Report')
        runner.run(test_suite)
        print('Test reports generate finished')


if __name__ == '__main__':
    StartTest.starttest()
