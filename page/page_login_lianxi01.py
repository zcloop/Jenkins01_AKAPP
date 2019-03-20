#把页面对象封装成类
class PageLogin():
    # 把单个页面元素的操作封装成方法
    def page_username_input(self,username):
        self.driver.find_element_by_id("").send_keys(username)

    def page_pwd_input(self,pwd):
        self.driver.find_element_by_id("").send_keys(pwd)

    def page_login_btn_click(self):
        self.driver.find_element_by_id("").click()

    #把页面元素的多个操作组装成一个方法
    def page_login(self,username,pwd):
        self.page_username_input(username)
        self.page_pwd_input(pwd)
        self.page_login_btn_click()