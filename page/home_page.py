from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 我 按钮
    me_btn = By.XPATH, "//*[@text='我']"

    # 点击 我
    def click_me(self):
        self.click(self.me_btn)