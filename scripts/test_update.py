import time


from base.base_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_update(self):
        self.page.home.click_me()

        # 调用没有登录去登录的方法
        self.page.home.login_if_not(self.page)

        # 我 - 点击设置按钮
        self.page.me.click_setting_btn()
        # 设置 - 滑动并点击 关于百年奥莱
        self.page.setting.click_about_aolai()
        # 关于 - 点击 版本更新
        self.page.about.click_version_update()
        # 断言 当前已是最新版本 toast信息是否存在
        assert self.page.about.is_toast_exist("当前已是最新版本")
