from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class BeVIPPage(BaseAction):

    # 输入框 特征
    input_feature = By.XPATH, "//input[@type='tel']"

    # 输入 验证码
    def input_verify_code(self, code):
        self.input(self.input_feature, code)

    # 立即成为会员 按钮 特征
    be_vip_submit_btn = By.XPATH, "//input[@value='立即成为会员']"

    # 点击立即成为会员
    def click_be_vip(self):
        self.click(self.be_vip_submit_btn)
