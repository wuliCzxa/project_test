# from pywebio.input import input, PASSWORD, select
# from pywebio.output import put_text, put_buttons, put_html, popup, toast
# from pywebio import start_server
# import hashlib
# import sqlite3
#
#
# class CinemaDataProcessor:
#     def __init__(self, db_path):
#         self.db_path = db_path
#
#     def get_db_connection(self):
#         conn = sqlite3.connect(self.db_path)
#         conn.row_factory = sqlite3.Row
#         return conn
#
#     def create_tables(self):
#         conn = self.get_db_connection()
#         cursor = conn.cursor()
#
#         # 创建用户表
#         cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                             user_id INTEGER PRIMARY KEY,
#                             username TEXT UNIQUE,
#                             password TEXT,
#                             role TEXT
#                         )''')
#
#         # 创建电影信息表
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS movies (
#             movie_id INTEGER PRIMARY KEY,
#             movie_name TEXT,
#             director TEXT,
#             cast TEXT,
#             genre TEXT,
#             release_date TEXT,
#             duration INTEGER
#         )
#         ''')
#
#         conn.commit()
#         conn.close()
#
#     def register_user(self):
#         username = input("请输入用户名: ")
#         password = input("请输入密码: ", type=PASSWORD)
#         role = select("请选择角色: ", ['顾客', '管理人员'])
#
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         conn = self.get_db_connection()
#         cursor = conn.cursor()
#
#         try:
#             cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
#                            (username, hashed_password, role))
#             conn.commit()
#             toast("注册成功！", position='center', duration=3)
#         except sqlite3.IntegrityError:
#             toast("用户名已存在，请选择其他用户名。", position='center', duration=3)
#
#         conn.close()
#
#     def login_user(self):
#         username = input("请输入用户名: ")
#         password = input("请输入密码: ", type=PASSWORD)
#
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         conn = self.get_db_connection()
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
#         user = cursor.fetchone()
#
#         if user:
#             toast("登录成功！", position='center', duration=3)
#             return user
#         else:
#             toast("用户名或密码错误。", position='center', duration=3)
#             return None
#
#         conn.close()
#
#     def customer_page(self):
#         put_text("欢迎您，顾客！")
#         # Here you can add customer-specific functionalities
#
#     def admin_page(self):
#         put_text("欢迎您，管理人员！")
#         # Here you can add admin-specific functionalities
#
#
# def main():
#     processor = CinemaDataProcessor('电影院管理系统.db')
#     processor.create_tables()
#
#     while True:
#         choice = select("请选择操作：", ['注册', '登录', '退出'])
#
#         if choice == '注册':
#             processor.register_user()
#         elif choice == '登录':
#             user = processor.login_user()
#             if user:
#                 if user['role'] == '顾客':
#                     processor.customer_page()
#                 elif user['role'] == '管理人员':
#                     processor.admin_page()
#         elif choice == '退出':
#             put_text("谢谢使用！")
#             break
#
#
# if __name__ == '__main__':
#     start_server(main, port=8080)

from pywebio.input import input, PASSWORD, select
from pywebio.output import put_text, put_buttons, put_html, popup, toast, put_table
from pywebio import start_server
import hashlib
import sqlite3


class CinemaDataProcessor:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        conn = self.get_db_connection()
        cursor = conn.cursor()

        # 创建用户表
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE,
                            password TEXT,
                            role TEXT
                        )''')

        # 创建电影信息表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER PRIMARY KEY,
            movie_name TEXT,
            director TEXT,
            cast TEXT,
            genre TEXT,
            release_date TEXT,
            duration INTEGER
        )
        ''')

        conn.commit()
        conn.close()

    def register_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ", type=PASSWORD)
        role = select("请选择角色: ", ['顾客', '管理人员'])

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = self.get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           (username, hashed_password, role))
            conn.commit()
            toast("注册成功！", position='center', duration=3)
        except sqlite3.IntegrityError:
            toast("用户名已存在，请选择其他用户名。", position='center', duration=3)

        conn.close()

    def login_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ", type=PASSWORD)

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = self.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = cursor.fetchone()

        if user:
            toast("登录成功！", position='center', duration=3)
            return user
        else:
            toast("用户名或密码错误。", position='center', duration=3)
            return None

        conn.close()

    def customer_page(self):
        while True:
            choice = select("请选择操作：", ['查看电影信息', '查看影票信息', '退出'])

            if choice == '查看电影信息':
                conn = self.get_db_connection()
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movies')
                movies = cursor.fetchall()
                put_table(movies, header=['电影ID', '电影名称', '导演', '演员阵容', '类型', '上映日期', '时长'])
                conn.close()
            elif choice == '查看影票信息':
                # Add functionality to view ticket information
                pass
            elif choice == '退出':
                break

    def admin_page(self):
        while True:
            choice = select("请选择操作：", ['查看电影信息', '查看影票信息', '添加电影', '添加顾客', '退出'])

            if choice == '查看电影信息':
                conn = self.get_db_connection()
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM movies')
                movies = cursor.fetchall()
                put_table(movies, header=['电影ID', '电影名称', '导演', '演员阵容', '类型', '上映日期', '时长'])
                conn.close()
            elif choice == '查看影票信息':
                # Add functionality to view ticket information
                pass
            elif choice == '添加电影':
                # Add functionality to add a movie
                pass
            elif choice == '添加顾客':
                # Add functionality to add a customer
                pass
            elif choice == '退出':
                break


def main():
    processor = CinemaDataProcessor('电影院管理系统.db')
    processor.create_tables()

    while True:
        choice = select("请选择操作：", ['注册', '登录', '退出'])

        if choice == '注册':
            processor.register_user()
        elif choice == '登录':
            user = processor.login_user()
            if user:
                if user['role'] == '顾客':
                    processor.customer_page()
                elif user['role'] == '管理人员':
                    processor.admin_page()
        elif choice == '退出':
            put_text("谢谢使用！")
            break


if __name__ == '__main__':
    start_server(main, port=8080)

