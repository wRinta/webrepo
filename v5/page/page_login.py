from po.v5 import page
from po.v5.base.base import Base


class PageLogin(Base):
    # 针对页面的元素设计单独的方法
    # 点击登录链接地址
    def page_click_login_link(self):
        self.base_click(page.link)
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)
    # 组装
    def page_login(self):