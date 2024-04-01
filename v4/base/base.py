"""
解包只需一次，在查找元素解包
drvier为虚拟，谁调用base传入
真正使用loc的方法只有查找元素方法使用
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Base:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            'https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=304792042703_0_d93d9359f3ec48de92fb4158be671ab5')

    # 查找元素方法（提供：点击、输入、获取文本)
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        # 封装显示等待,显示等待会返回元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空内容
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_img(self):
        self.driver.get_screenshot_as_file("../imge/fail3.png")
