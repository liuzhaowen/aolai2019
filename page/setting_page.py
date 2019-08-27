from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 关于百年奥莱 按钮
    about_aolai_feature = By.XPATH, "//*[@text='关于百年奥莱']"

    # 找到并点击关于百年奥莱
    def click_about_aolai(self):
        self.find_element_with_scroll(self.about_aolai_feature).click()