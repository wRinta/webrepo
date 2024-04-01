# 导包
import unittest

from parameterized import parameterized

from po.v4.page.page_login import PageLogin


def get_data():
    return [('13345678899', '123456', '账号不存在'), ('15945678899', '123123', '密码错误')]


# 新建测试类并继承
class TestLogin(unittest.TestCase):
    login = None

    # setUP
    @classmethod
    def setUpClass(cls):
        # 实例化获取页面对象PageLogin
        cls.login = PageLogin()
        # 点击登录
        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭驱动对象
        cls.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect):
        # 调用登录方法
        self.login.page_login(username, pwd)
        # 获取登录提示信息
        msg = self.login.page_get_text()
        # 断言
        try:
            self.assertEqual(msg, expect)
        except AssertionError:
            # 截图
            self.login.page_get_screenshot()
