from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 昵称的特征
    nick_name_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 设置按钮 特征
    setting_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 加入超级VIP 特征
    join_VIP_btn = By.XPATH, "//*[@text='加入超级VIP']"


    # 获取昵称信息
    def get_nick_name(self):
        return self.get_text(self.nick_name_feature)

    # 点击设置按钮
    def click_setting_btn(self):
        self.click(self.setting_btn)

    # 点击加入超级VIP
    def click_join_VIP(self):
        self.find_element_with_scroll(self.join_VIP_btn).click()