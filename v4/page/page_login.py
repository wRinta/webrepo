from po.v4 import page
from po.v4.base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常信息
    def page_get_text(self):
        return self.base_get_text(page.login_msg)

    # 截图
    def page_get_screenshot(self):
        self.base_get_img()

    # 组装
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
