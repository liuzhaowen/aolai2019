from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 我 按钮
    me_btn = By.XPATH, "//*[@text='我']"

    # 点击 我
    def click_me(self):
        self.click(self.me_btn)

    # 如果没有登录则登录
    def login_if_not(self, page):
        # 判断当前界面是否是注册页面
        if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.LogonActivity":
            # 如果是，则进行登录操作
            # register - 点击去登录
            page.register.click_to_login()
            # login - 输入用户名
            page.login.input_username("itheima_test")
            # login - 输入密码
            page.login.input_password("itheima")
            # login - 点击登录
            page.login.click_login_btn()
        # 如果不是，什么都不需要操作