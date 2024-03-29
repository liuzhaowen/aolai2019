from appium import webdriver


def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

    # 默认不重置
    desired_caps['noReset'] = no_reset
    # toast
    desired_caps['automationName'] = 'Uiautomator2'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
