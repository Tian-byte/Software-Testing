"""
    模块名：page_模块单词
    类名：大驼峰将模块移植进来，去掉下划线和数字。
    方法：自动化测试当前页面要操作那些元素，就封装那些方法
"""
from selenium.webdriver.common.by import By

from Base.base import Base

# 用户名


username = (By.CSS_SELECTOR, "#username")
# 密码
pwd = By.CSS_SELECTOR, "#password"
# 验证码
verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 昵称
nick_name = By.CSS_SELECTOR, ".userinfo"


class PageLogin(Base):
    # 输入用户名
    def __page_username(self, value):
        self.base_input(username, value)

    # 输入密码
    def __page_pwd(self, value):
        self.base_input(pwd, value)

    # 输入验证码
    def __page_verify_code(self, value):
        self.base_input(verify_code, value)

    # 点击登录按钮
    def __page_click_login_btn(self):
        self.base_click(login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(nick_name)

    # 组合业务方法 （强调：测试业务成调用此方法，便捷。）
    def page_login(self, phone, password, code):
        self.__page_username(phone)
        self.__page_pwd(password)
        self.__page_verify_code(code)
        self.__page_click_login_btn()
