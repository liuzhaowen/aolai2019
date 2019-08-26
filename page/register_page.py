from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):

    # 去登录
    to_login_btn = By.XPATH, "//*[contains(@text, '已有账号')]"

    # 点击去登录
    def click_to_login(self):
        self.click(self.to_login_btn)