# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver

    def findElement(self, locator, timeout=30):
        '''
        locator 参数是定位方式，如("id", "kw")， 把两个参数合并为一个
        *号是把两个参数分开传值
        Usage:
            locator = ("id", "kw")
            driver.find_element(*locator)
        '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print('正在定位元素信息： 定位方式-> %s, value值-> %s' %(locator[0], locator[1]))
            element = WebDriverWait(self.driver, timeout, 1).until(lambda x: x.find_element(*locator))
            return element

    def findElements(self, locator, timeout=30):
        '''
        :param locator: 传元祖, 如("id","xx")
        :return:
        '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print('正在定位元素信息： 定位方式-> %s, value值-> %s' %(locator[0], locator[1]))
            elements = WebDriverWait(self.driver, timeout, 1).until(lambda x:x.find_element(*locator))
            return elements

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def sendKeys(self, locator, text, is_clear_first=False):
        '''
        输入内容
        :param locator: 元素
        :param text: 输入的内容
        :param is_clear_first  默认为False，不清空输入框
        :return:
        '''
        ele = self.findElement(locator)
        if is_clear_first:
            ele.clear()    # is_clear_first 为True的时候执行
        ele.send_keys(text)

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def is_element_exist(self, locator):
        '''查找元素的时候，存在返回element，不存在的时候Timeout异常了'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_elements_exist(self, locator):
        els = self.findElement(locator)
        count = len(els)   # 计算元素个数
        if count == 0:
            return False
        elif count == 1:
            return True
        else:
            print('定位到元素个数： %s', count)
            return True

    def is_text_in_element(self, locator, text, timeout=5):
        '''
        10秒内循环判断元素中是否包含文本，循环判断成功返回True，失败会抛超时异常
        :param locator:元素
        :param text:文本
        :param timeout:超时时间
        :return:
        '''
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def is_alert(self, timeout=10):
        '''
        判断页面是否有alert，有返回alert，不是True
        每页返回False
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present)
            return result
        except:
            return False

    def switch_handle(self, window_name):
        '''切换句柄'''
        self.driver.switch_to.window(window_name)

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element(locator)
        '''
        try:
            element = self.findElement(locator)
        except TimeoutException:
            print("element not found: %s" % locator)
        else:
            ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)    # 定位select这一栏的元素
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element =  self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def js_scroll_end(self):
        '''滚动到底部，一般不需要横向滚动'''
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"   # 自动计算高度，最上方是0
        self.driver.execute_script(js_heig)

    def js_focus_element(self, locator):
        '''聚焦元素，滚动到元素出现的位置，最实用'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print('获取text失败，返回""')
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print('获取get_attribute失败，返回""')
            return ""