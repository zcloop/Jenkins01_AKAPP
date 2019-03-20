#定义基类
#主要封装一些公共操作方法
from selenium.webdriver.support.wait import WebDriverWait

from base import get_driver


class Base(): #类名是直接以大驼峰的形式把模块文件名抄进来，省略下划线
    # 初始化驱动driver
    def __init__(self,driver):
        self.driver = driver

    # 定义基础方法 -- 方法名以base开头便于后期调用
    # 查找元素方法 封装
    def base_find_element(self,loc,timeout=30,poll_frequency=0.5): #loc 定位元素(元组) BY.XX,"定位元素的字符串"
        # 设置显示等待同时定位元素 -- *loc中的*用来解包元组
        WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x: x.find_element(*loc))
    #点击元素方法 封装
    def base_click_element(self,loc):
        self.base_find_element(loc).click()

    #输入元素方法 封装
    def base_input_element(self,loc,value):
        #定位元素
        ele = self.base_find_element(loc)
        ele.clear() #清空
        ele.send_keys(value) #输入内容
