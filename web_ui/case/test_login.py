# coding=utf-8
import unittest
from selenium import webdriver
from pages.login_page import LoginPage, login_url

'''
1.输入admin, 输入123456 点登录 （错误的账号和密码）
2.输入admin, 输入      点登录
3.点忘记密码
'''


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        '''让每一个用例回到起点,回到登录页'''
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()    # 退出登录，删除浏览器所有的cookies
        self.driver.refresh()

    def test_01(self):
        '''1.输入admin, 输入123456 点登录'''
        self.loginp.input_user('admin')
        self.loginp.input_psw('123456')
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        # 断言  登录失败
        self.assertTrue(result == "admin")

    def test_02(self):
        '''2.输入admin, 输入      点登录'''
        self.loginp.input_user('admin')
        self.loginp.click_login_button()
        result =self.loginp.get_login_name()
        # 断言
        self.assertTrue(result == "")

    def test_03(self):
        '''3.点忘记密码'''
        self.loginp.click_forget_psw()
        result = self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()