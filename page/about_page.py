from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    # 版本更新 按钮
    version_update_btn = By.XPATH, "//*[@text='版本更新']"

    # 点击版本更新 按钮
    def click_version_update(self):
        self.click(self.version_update_btn)
