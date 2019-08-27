import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):

        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # home - 点击我
        self.page.home.click_me()
        # register - 点击去登录
        self.page.register.click_to_login()
        # login - 输入用户名
        self.page.login.input_username(username)
        # login - 输入密码
        self.page.login.input_password(password)
        # login - 点击登录
        self.page.login.click_login_btn()

        # 断言操作
        if not toast:
            assert self.page.me.get_nick_name() == "itheima_test"
        else:
            assert self.page.login.is_toast_exist(toast)