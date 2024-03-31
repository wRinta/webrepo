from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self):
        # 获取driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            'https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=304792042703_0_d93d9359f3ec48de92fb4158be671ab5')

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        # 获取元素并进行点击
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
