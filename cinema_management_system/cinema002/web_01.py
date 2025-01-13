from pywebio.input import input, PASSWORD, select, radio
from pywebio.output import put_text, put_buttons, put_error
import hashlib

from test import CinemaDataProcessor

class CinemaWebApp:
    def __init__(self, db_path):
        self.processor = CinemaDataProcessor(db_path)

    def register_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ", type=PASSWORD)

        # 对密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 注册用户并指定角色
        role = input("请选择角色（顾客/管理人员）: ")
        if role not in ['顾客', '管理人员']:
            put_error("无效的角色选择")
            return
        self.processor.register_user(username, hashed_password, role)
        put_text("注册成功！")

    def login_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ", type=PASSWORD)

        # 对密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 登录用户
        user_role = self.processor.login_user(username, hashed_password)
        if user_role:
            put_text("登录成功！")
            return user_role
        else:
            put_error("用户名或密码错误。")
            return None

    def customer_page(self):
        put_text("欢迎来到顾客页面！")
        # 添加顾客页面具体内容

    def manager_page(self):
        put_text("欢迎来到管理人员页面！")
        # 添加管理人员页面具体内容

# 如果需要测试，可以在此处添加测试代码
if __name__ == '__main__':
    app = CinemaWebApp('test.db')
    app.register_user()
    app.login_user()
