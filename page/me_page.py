from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 昵称的特征
    nick_name_feature = By.ID, "com.yunmall.lc:id/tv_user_nikename"


    # 获取昵称信息
    def get_nick_name(self):
        return self.get_text(self.nick_name_feature)