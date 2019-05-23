# coding = utf-8
from common.base import Base

# 仅用于学习 详见网页：www.istester.com
login_url = 'http://zentao.istester.com/user-login'


class LoginPage(Base):
    # 定位登录
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_button = ("id", "submit")

    loc_keep_login = ("id", "keepLoginon")            # 保持登录
    loc_forget_psw = ("link text", "忘记密码")            # 忘记密码

    loc_get_user = ("css selector", "#userMenu>a")      # 获取账号名称
    loc_forget_psw = ("css selector", ".btn")      # 获取账号名称

    def input_user(self, text=""):
        '''输入账号'''
        self.sendKeys(self.loc_user, text)

    def input_psw(self, text=""):
        '''输入密码'''
        self.sendKeys(self.loc_psw, text)

    def click_login_button(self):
        '''登录按钮'''
        self.click(self.loc_button)

    def click_keep_login(self):
        '''保持登录'''
        self.click(self.loc_keep_login)

    def click_forget_psw(self):
        '''忘记密码'''
        self.click(self.loc_forget_psw)

    def login(self, user='admin', psw='123456', keep_login=False):
        '''登录流程'''
        self.driver.get(login_url)
        self.sendKeys(self.loc_user, user)
        self.sendKeys(self.loc_psw, psw)

        if keep_login:
            self.click(self.loc_keep_login)

        self.click(self.loc_button)

    def get_login_name(self):
        '''获取登录的名称'''
        user = self.get_text(self.loc_get_user)
        return user

    def get_login_result(self, user):
        '''获取登录测试结果'''
        result = self.is_text_in_element(self.loc_get_user, user)
        return result

    def is_alert_exist(self):
        '''判断alert是不是在'''
        # try:
        #     time.sleep(2)
        #     alert = self.driver.switch_to.alert
        #     text = alert.text
        #     alert.accept()     # 用alert  点alert
        #     return text
        # except:
        #     return ""

        # 可以直接从base里面调用
        a = self.is_alert()
        if a:
            '''存在的话接收'''
            print('alert的text: ', a.text)
            a.accept()

    def is_refresh_exist(self):
        '''判断忘记密码页，刷新按钮是否存在'''
        r = self.is_element_exist(self.loc_forget_psw)
        return r


