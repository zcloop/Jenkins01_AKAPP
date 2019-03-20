"""
把页面Page封装成一个类（即一个页面就是一个对象）；
定义类-类名是以大驼峰的方式把模块文件名抄进来，省略下划线；PageLogin
定义方法-把页面元素的每一个操作都封装成一个方法
"""
#把页面定义成类
from selenium.webdriver.common.by import By

from base.base import Base

#元素定位所需参数暂存
loc_username = By.ID,"com.vcooline.aike:id/etxt_username"
loc_pwd = By.ID,"com.vcooline.aike:id/etxt_pwd"
loc_btn = By.ID,"com.vcooline.aike:id/btn_login"


class PageLogin(Base): #页面类继承基类中的方法和实例属性
    #每一步操作封装成一个方法
    #输入用户名
    def page_input_username(self,username):
        #调用继承自基类中的输入内容方法即可
        self.base_input_element(loc_username,username)

    #输入密码
    def page_input_pwd(self,pwd):
        self.base_input_element(loc_pwd, pwd)

    #点击登录按钮
    def page_click_login_btn(self):
        self.base_click_element(loc_btn)

    #组装登录方法
    def page_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

