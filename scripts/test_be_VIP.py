import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestBeVIP:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("be_vip_data.yaml", "test_be_vip"))
    def test_be_vip(self, args):

        keyword = args["keyword"]
        expect = args["expect"]

        # home - 点击我
        self.page.home.click_me()
        # home - 如果没有登录则登录
        self.page.home.login_if_not(self.page)
        # me - 点击 加入超级VIP按钮
        self.page.me.click_join_VIP()

        # 等待webview 加入超级VIP页面加载
        time.sleep(10)
        # print(self.driver.contexts)
        # ['NATIVE_APP', 'WEBVIEW_com.yunmall.lc']
        # 切换 上下文
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # be_vip - 输入验证码
        self.page.be_vip.input_verify_code(keyword)
        # be_vip - 点击 立即成为会员按钮
        self.page.be_vip.click_be_vip()
        # be_vip - 断言响应 信息
        assert self.page.be_vip.is_keyword_in_page_source(expect)
        # 切换为 原来的上下文
        self.driver.switch_to.context("NATIVE_APP")
