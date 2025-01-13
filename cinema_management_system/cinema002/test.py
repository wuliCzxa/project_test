import sqlite3
import pandas as pd
import shutil
import hashlib

class CinemaDataProcessor:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    # 创建用户表
    def create_user_table(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            role TEXT NOT NULL
                        )''')
        conn.commit()
        conn.close()

    # 用户注册
    def register_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        role = input("请输入角色（customer/manager）: ")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = sqlite3.connect('电影院管理系统.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
            conn.commit()
            print("注册成功！")
            conn.close()
        except sqlite3.IntegrityError:
            print("用户名已存在，请选择其他用户名。")

    # 用户登录
    def login_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            print("登录成功！")
        else:
            print("用户名或密码错误。")

    def create_tables(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL,
                            role TEXT NOT NULL
                        )''')

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

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT,
            age INTEGER,
            phone TEXT,
            email TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            customer_id INTEGER,
            screening_id INTEGER,
            seat_number TEXT,
            price REAL,
            FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (screening_id) REFERENCES screenings (screening_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS screenings (
            screening_id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            screening_room TEXT,
            screening_time TEXT,
            status TEXT,
            FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
        )
        ''')

        conn.commit()
        conn.close()

    # 主菜单
    def main_menu(self):
        while True:
            print("1. 查询数据")
            print("2. 插入数据")
            print("3. 更新数据")
            print("4. 删除数据")
            print("5. 备份数据")
            print("6. 用户注册")
            print("7. 用户登录")
            print("8. 其他操作")
            print("0. 退出程序")

            choice = input("请输入选项: ")

            if choice == '1':
                self.query_data()
            elif choice == '2':
                self.insert_data()
            elif choice == '3':
                self.update_data()
            elif choice == '4':
                self.delete_data()
            elif choice == '5':
                self.backup_data()
            elif choice == '6':
                self.register_user()
            elif choice == '7':
                self.login_user()
            elif choice == '8':
                self.operation_user()
            elif choice == '0':
                print("退出程序")
                break
            else:
                print("无效输入，请重新输入")

    # 查询数据的函数
    def query_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要查询的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())

        if table_num == 1:
            self.query_movies()
        elif table_num == 2:
            self.query_customers()
        elif table_num == 3:
            self.query_tickets()
        elif table_num == 4:
            self.query_screenings()

        conn.close()

    def query_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        print("\n电影信息：")
        for movie in movies:
            print(movie)

        conn.close()

    def query_customers(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        print("\n顾客信息：")
        for customer in customers:
            print(customer)

        conn.close()

    def query_tickets(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM tickets')
        tickets = cursor.fetchall()
        print("\n影票信息：")
        for ticket in tickets:
            print(ticket)

        conn.close()

    def query_screenings(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM screenings')
        screenings = cursor.fetchall()
        print("\n放映信息：")
        for screening in screenings:
            print(screening)

        conn.close()

    def insert_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要插入的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())

        if table_num == 1:
            self.insert_movies()
        elif table_num == 2:
            self.insert_customers()
        elif table_num == 3:
            self.insert_tickets()
        elif table_num == 4:
            self.insert_screenings()

        conn.close()

    def insert_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            movies_df = pd.read_excel('movies.xlsm')
            movies_df.to_sql('movies', conn, if_exists='append', index=False)
        elif choice == 2:
            movie_id = int(input("请输入电影ID: "))
            movie_name = input("请输入电影名称: ")
            director = input("请输入导演姓名：")
            cast = input("请输入演员阵容：")
            genre = input("请输入类型：")
            release_date = input("请输入上映时间：")
            duration = input("请输入电影时长：")
            cursor.execute('INSERT INTO movies (movie_id, movie_name,director,cast,genre,release_date,duration) VALUES (?, ?, ?, ?, ?, ?, ?)', (movie_id, movie_name,director,cast,genre,release_date,duration))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("电影信息已插入")
        conn.close()

    def insert_customers(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            customers_df = pd.read_excel('customers.xlsm')
            customers_df.to_sql('customers', conn, if_exists='append', index=False)
        elif choice == 2:
            customer_id = int(input("请输入顾客ID: "))
            name = input("请输入顾客姓名: ")
            cursor.execute('INSERT INTO customers (customer_id, name) VALUES (?, ?)', (customer_id, name))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("顾客信息已插入")
        conn.close()

    def insert_tickets(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            tickets_df = pd.read_excel('tickets.xlsm')
            tickets_df.to_sql('tickets', conn, if_exists='append', index=False)
        elif choice == 2:
            ticket_id = int(input("请输入影票ID: "))
            movie_id = int(input("请输入电影ID: "))
            customer_id = int(input("请输入顾客ID: "))
            cursor.execute('INSERT INTO tickets (ticket_id, movie_id, customer_id) VALUES (?, ?, ?)', (ticket_id, movie_id, customer_id))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("影票信息已插入")
        conn.close()

    def insert_screenings(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            screenings_df = pd.read_excel('screenings.xlsm')
            screenings_df.to_sql('screenings', conn, if_exists='append', index=False)
        elif choice == 2:
            screening_id = int(input("请输入放映ID: "))
            movie_id = int(input("请输入电影ID: "))
            screening_room = input("请输入放映厅: ")
            screening_time = input("请输入放映时间: ")
            status = input("请输入状态: ")
            cursor.execute('INSERT INTO screenings (screening_id, movie_id, screening_room, screening_time, status) VALUES (?, ?, ?, ?, ?)', (screening_id, movie_id, screening_room, screening_time, status))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("放映信息已插入")
        conn.close()

    def update_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())

        if table_num == 1:
            self.update_movies()
        elif table_num == 2:
            self.update_customers()
        elif table_num == 3:
            self.update_tickets()
        elif table_num == 4:
            self.update_screenings()

        conn.close()

    def update_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的电影ID：")
        movie_id = int(input("电影ID: "))
        new_name = input("新的电影名称: ")
        new_director = input("新的导演: ")
        new_cast = input("新的演员阵容: ")
        new_genre = input("新的类型: ")
        new_release_date = input("新的上映日期: ")
        new_duration = int(input("新的时长: "))

        cursor.execute('''
        UPDATE movies
        SET movie_name = ?,
            director = ?,
            cast = ?,
            genre = ?,
            release_date = ?,
            duration = ?
        WHERE movie_id = ?
        ''', (new_name, new_director, new_cast, new_genre, new_release_date, new_duration, movie_id))

        conn.commit()
        print("电影信息已更新")

        conn.close()

    def update_customers(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的顾客ID：")
        customer_id = int(input("顾客ID: "))
        new_name = input("新的顾客姓名: ")
        new_gender = input("新的顾客性别: ")
        new_age = int(input("新的顾客年龄: "))
        new_phone = input("新的顾客电话: ")
        new_email = input("新的顾客邮箱: ")
        cursor.execute('''
            UPDATE customers
            SET name = ?,
                gender = ?,
                age = ?,
                phone = ?,
                email = ?
            WHERE customer_id = ?
            ''', (new_name, new_gender, new_age, new_phone, new_email, customer_id))

        conn.commit()
        print("顾客信息已更新")

        conn.close()

    def update_tickets(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的影票ID：")
        ticket_id = int(input("影票ID: "))
        new_movie_id = int(input("新的电影ID: "))
        new_customer_id = int(input("新的顾客ID: "))
        new_screening_id = int(input("新的放映ID: "))
        new_seat_number = input("新的座位号: ")
        new_price = float(input("新的票价: "))

        cursor.execute('''
            UPDATE tickets
            SET movie_id = ?,
                customer_id = ?,
                screening_id = ?,
                seat_number = ?,
                price = ?
            WHERE ticket_id = ?
            ''', (new_movie_id, new_customer_id, new_screening_id, new_seat_number, new_price, ticket_id))

        conn.commit()
        print("影票信息已更新")

        conn.close()

    def update_screenings(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的放映ID：")
        screening_id = int(input("放映ID: "))
        new_movie_id = int(input("新的电影ID: "))
        new_screening_room = input("新的放映厅: ")
        new_screening_time = input("新的放映时间: ")
        new_status = input("新的状态: ")

        cursor.execute('''
            UPDATE screenings
            SET movie_id = ?,
                screening_room = ?,
                screening_time = ?,
                status = ?
            WHERE screening_id = ?
            ''', (new_movie_id, new_screening_room, new_screening_time, new_status, screening_id))

        conn.commit()
        print("放映信息已更新")

        conn.close()

    def delete_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要删除的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())

        if table_num == 1:
            self.delete_movies()
        elif table_num == 2:
            self.delete_customers()
        elif table_num == 3:
            self.delete_tickets()
        elif table_num == 4:
            self.delete_screenings()

        conn.close()

    def delete_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        movie_id = int(input("请输入要删除的电影ID: "))

        cursor.execute('''
            DELETE FROM movies
            WHERE movie_id = ?
            ''', (movie_id,))

        conn.commit()
        print("电影信息已删除")

        conn.close()

    def delete_customers(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        customer_id = int(input("请输入要删除的顾客ID: "))

        cursor.execute('''
            DELETE FROM customers
            WHERE customer_id = ?
            ''', (customer_id,))

        conn.commit()
        print("顾客信息已删除")

        conn.close()

    def delete_tickets(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        ticket_id = int(input("请输入要删除的影票ID: "))

        cursor.execute('''
            DELETE FROM tickets
            WHERE ticket_id = ?
            ''', (ticket_id,))

        conn.commit()
        print("影票信息已删除")

        conn.close()

    def delete_screenings(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        screening_id = int(input("请输入要删除的放映ID: "))

        cursor.execute('''
            DELETE FROM screenings
            WHERE screening_id = ?
            ''', (screening_id,))

        conn.commit()
        print("放映信息已删除")

        conn.close()

    def backup_data(self):
        shutil.copyfile('电影院管理系统.db', '电影院管理系统_backup.db')
        print("数据库备份完成")

    def operation_user(self):
        pass

if __name__ == '__main__':
    processor = CinemaDataProcessor('电影院管理系统.db')
    processor.create_tables()
    processor.main_menu()
