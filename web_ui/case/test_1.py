# coding=utf-8
from selenium import webdriver
from common.base import Base
import time
import unittest


class GanJiTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.b = Base(self.driver)
        self.driver.get('http://bj.ganji.com/')

    def test_focus_element(self):
        """聚焦元素"""
        time.sleep(3)
        self.b.js_focus_element(('link text', '新车'))

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()