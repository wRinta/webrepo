from selenium.webdriver.common.by import By

# 以下为登录页面元素配置信息
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"

# 用户名
login_username = By.CSS_SELECTOR, "#loginname"
# 密码
login_pwd = By.CSS_SELECTOR, "#nloginpwd"
# 点击按钮
login_btn = By.CSS_SELECTOR, "#loginsubmit"
# 提示信息
login_msg = By.CSS_SELECTOR, ".msg-error"