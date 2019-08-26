import time

from base.base_driver import init_driver


class TestDemo:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_demo(self):
        pass