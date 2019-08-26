from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 账号输入框 特征
    username_input = By.ID, "com.yunmall.lc:id/logon_account_textview"

    # 密码框 特征
    password_input = By.ID, "com.yunmall.lc:id/logon_password_textview"

    # 登录按钮 特征
    login_btn = By.ID, "com.yunmall.lc:id/logon_button"

    # 输入用户名
    def input_username(self, username):
        self.input(self.username_input, username)

    # 输入密码
    def input_password(self, password):
        self.input(self.password_input, password)

    # 点击登录
    def click_login_btn(self):
        self.click(self.login_btn)