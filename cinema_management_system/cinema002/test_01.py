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

    # 连接到数据库
    conn = sqlite3.connect('电影院管理系统.db')
    c = conn.cursor()

    # 创建用户表
    def create_user_table(self):
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                    )''')
        conn.commit()

    # 用户注册
    def register_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")

        # 对密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 尝试插入新用户信息到数据库
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print("注册成功！")
        except sqlite3.IntegrityError:
            print("用户名已存在，请选择其他用户名。")

    # 用户登录
    def login_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")

        # 对密码进行哈希处理
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # 查询数据库中是否存在匹配的用户名和密码
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = c.fetchone()

        if user:
            print("登录成功！")
        else:
            print("用户名或密码错误。")

    def operation_user(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()
        print("请输入要进行的操作：")
        print("1. 查询整个用户表")
        print("2. 查询特定用户")
        print("3. 插入用户")
        print("4. 更新用户密码")
        print("5. 删除用户")
        table_num = int(input())
        if table_num == 1:
            query_all_users()
        elif table_num == 2:
            query_user_by_id()
        elif table_num == 3:
            insert_user()
        elif table_num == 4:
            update_user_password()
        elif table_num == 5:
            delete_user_by_id()

        conn.close()

    # 查询整个用户表
    def query_all_users(self):
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        for user in users:
            print(user)

    # 查询特定用户
    def query_user_by_id(self):
        user_id = input("请输入要查询的用户ID: ")
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = c.fetchone()
        if user:
            print(user)
        else:
            print("未找到该用户")

    # 插入用户
    def insert_user(self):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print("用户添加成功！")
        except sqlite3.IntegrityError:
            print("用户名已存在，请选择其他用户名。")

    # 更新用户密码
    def update_user_password(self):
        user_id = input("请输入要更新密码的用户ID: ")
        new_password = input("请输入新密码: ")
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        c.execute("UPDATE users SET password=? WHERE id=?", (hashed_password, user_id))
        conn.commit()
        print("密码更新成功！")

    # 删除用户
    def delete_user_by_id(self):
        user_id = input("请输入要删除的用户ID: ")
        c.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        print("用户删除成功！")

    def create_tables(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()
        create_user_table()

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

        # 创建顾客信息表
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

        # 创建影票信息表
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

        # 创建放映信息表
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

    # def insert_data():
    #     conn = sqlite3.connect('电影院管理系统.db')
    #     cursor = conn.cursor()
    #
    #     # 从xlsm文件中读取数据并插入到表中
    #     movies_df = pd.read_excel('movies.xlsm')
    #     movies_df.to_sql('movies', conn, if_exists='append', index=False)
    #
    #     customers_df = pd.read_excel('customers.xlsm')
    #     customers_df.to_sql('customers', conn, if_exists='append', index=False)
    #
    #     tickets_df = pd.read_excel('tickets.xlsm')
    #     tickets_df.to_sql('tickets', conn, if_exists='append', index=False)
    #
    #     screenings_df = pd.read_excel('screenings.xlsm')
    #     screenings_df.to_sql('screenings', conn, if_exists='append', index=False)
    #
    #     conn.close()


    # 查找数据的函数

    def query_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        # print("请输入要执行的操作序号：")
        # # print("1. 查询数据")
        # # print("2. 插入数据")
        # # print("3. 更新数据")
        # # print("4. 删除数据")
        # # print("5. 备份数据")
        # action_num = int(input())
        #
        # if action_num == 1:
        print("请输入要查询的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())
        if table_num == 1:
            print("请问进行整表操作or操作行数据")
            print("1. 整表操作")
            print("2. 行数据操作")
            table_num_1 = int(input())
            if table_num_1 == 1:
                query_movies()
            elif table_num_1 == 2:
                movie_id = input("请输入电影ID: ")
                query_movies_id(movie_id)
        elif table_num == 2:
            print("请问进行整表操作or操作行数据")
            print("1. 整表操作")
            print("2. 行数据操作")
            table_num_2 = int(input())
            if table_num_2 == 1:
                query_customers()
            elif table_num_2 == 2:
                customer_id = input("请输入顾客ID: ")
                query_customers_id(customer_id)
        elif table_num == 3:
            print("请问进行整表操作or操作行数据")
            print("1. 整表操作")
            print("2. 行数据操作")
            table_num_3 = int(input())
            if table_num_3 == 1:
                query_tickets()
            elif table_num_3 == 2:
                ticket_id = input("请输入影票ID: ")
                query_tickets_id(ticket_id)
        elif table_num == 4:
            print("请问进行整表操作or操作行数据")
            print("1. 整表操作")
            print("2. 行数据操作")
            table_num_4 = int(input())
            if table_num_4 == 1:
                query_screenings()
            elif table_num_4 == 2:
                screening_id = input("请输入放映ID: ")
                query_screenings_id(screening_id)
        # elif action_num == 3:
        #     update_data()
        # elif action_num == 4:
        #     delete_data()
        # elif action_num == 5:
        #     backup_data()

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

    def query_movies_id(movie_id):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM movies WHERE rowid=?', (movie_id,))
        movie = cursor.fetchone()
        if movie:
            print("\n电影信息：")
            print(movie)
        else:
            print("未找到该电影")

        conn.close()

    def query_customers_id(customer_id):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM customers WHERE rowid=?', (customer_id,))
        customer = cursor.fetchone()
        if customer:
            print("\n顾客信息：")
            print(customer)
        else:
            print("未找到该顾客")

        conn.close()

    def query_tickets_id(ticket_id):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM tickets WHERE rowid=?', (ticket_id,))
        ticket = cursor.fetchone()
        if ticket:
            print("\n影票信息：")
            print(ticket)
        else:
            print("未找到该影票")

        conn.close()

    def query_screenings_id(screening_id):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM screenings WHERE rowid=?', (screening_id,))
        screening = cursor.fetchone()
        if screening:
            print("\n放映信息：")
            print(screening)
        else:
            print("未找到该放映信息")

        conn.close()


    #插入数据的函数
    def insert_data(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        # 从xlsm文件中读取数据并插入到表中

        print("请输入要插入的表的序号：")
        print("1. 电影信息表")
        print("2. 顾客信息表")
        print("3. 影票信息表")
        print("4. 放映信息表")
        table_num = int(input())

        if table_num == 1:
            insert_movies()
        elif table_num == 2:
            insert_customers()
        elif table_num == 3:
            insert_tickets()
        elif table_num == 4:
            insert_screenings()

        conn.close()

    def insert_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            # 整表操作示例：从文件中读取电影数据并插入
            movies_df = pd.read_excel('movies.xlsm')
            movies_df.to_sql('movies', conn, if_exists='append', index=False)
        elif choice == 2:
            # 行数据操作示例：手动输入电影ID并插入
            movie_id = int(input("请输入电影ID: "))
            movie_name = input("请输入电影名称: ")
            director = input("请输入导演姓名：")
            cast = input("请输入演员阵容：")
            gengre = input("请输入类型：")
            release_date = input("请输入上映时间：")
            duration = input("请输入电影时长：")
            cursor.execute('INSERT INTO movies (movie_id, movie_name,director,cast,gengre,release_date,duration) VALUES (?, ?, ?, ?, ?, ?, ?)', (movie_id, movie_name,director,cast,gengre,release_date,duration))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("电影信息已插入")
        conn.close()


    # 插入顾客信息的函数
    def insert_customers(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            # 整表操作示例：从文件中读取顾客数据并插入
            customers_df = pd.read_excel('customers.xlsm')
            customers_df.to_sql('customers', conn, if_exists='append', index=False)
        elif choice == 2:
            # 行数据操作示例：手动输入顾客ID并插入
            customer_id = int(input("请输入顾客ID: "))
            name = input("请输入顾客姓名: ")
            cursor.execute('INSERT INTO customers (customer_id, name) VALUES (?, ?)', (customer_id, name))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("顾客信息已插入")
        conn.close()

    # 插入影票信息的函数
    def insert_tickets(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            # 整表操作示例：从文件中读取影票数据并插入
            tickets_df = pd.read_excel('tickets.xlsm')
            tickets_df.to_sql('tickets', conn, if_exists='append', index=False)
        elif choice == 2:
            # 行数据操作示例：手动输入影票ID并插入
            ticket_id = int(input("请输入影票ID: "))
            movie_id = int(input("请输入电影ID: "))
            customer_id = int(input("请输入顾客ID: "))
            cursor.execute('INSERT INTO tickets (ticket_id, movie_id, customer_id) VALUES (?, ?, ?)', (ticket_id, movie_id, customer_id))
        else:
            print("无效的选择，请重新选择。")

        conn.commit()
        print("影票信息已插入")
        conn.close()

    # 插入放映信息的函数
    def insert_screenings(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请选择插入方式：")
        print("1. 整表操作")
        print("2. 行数据操作")
        choice = int(input())

        if choice == 1:
            # 整表操作示例：从文件中读取放映数据并插入
            screenings_df = pd.read_excel('screenings.xlsm')
            screenings_df.to_sql('screenings', conn, if_exists='append', index=False)
        elif choice == 2:
            # 行数据操作示例：手动输入放映ID并插入
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


    #更新数据的函数
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
            update_movies()
        elif table_num == 2:
            update_customers()
        elif table_num == 3:
            update_tickets()
        elif table_num == 4:
            update_screenings()

        conn.close()

    def update_movies(self):
        conn = sqlite3.connect('电影院管理系统.db')
        cursor = conn.cursor()

        print("请输入要更新的电影ID：")
        movie_id = int(input("电影ID: "))
        new_name = input("新的电影名称: ")
        new_director = input("新的导演: ")
        new_cast = input("新的演员阵容: ")
        new_gengre = input("新的类型: ")
        new_release_date = input("新的上映日期: ")
        new_duration = int(input("新的时长: "))

        cursor.execute('''
        UPDATE movies
        SET movie_name = ?,
            director = ?,
            cast = ?,
            gengre = ?,
            release_date = ?,
            duration = ?
        WHERE movie_id = ?
        ''', (new_name, new_director, new_cast, new_gengre, new_release_date, new_duration, movie_id))

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


    #删除数据的函数

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
            delete_movies()
        elif table_num == 2:
            delete_customers()
        elif table_num == 3:
            delete_tickets()
        elif table_num == 4:
            delete_screenings()

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
        # 备份数据库文件
        shutil.copyfile('电影院管理系统.db', '电影院管理系统_backup.db')
        print("数据库备份完成")




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
                query_data()
            elif choice == '2':
                insert_data()
            elif choice == '3':
                update_data()
            elif choice == '4':
                delete_data()
            elif choice == '5':
                backup_data()
            elif choice == '6':
                register_user()
            elif choice == '7':
                login_user()
            elif choice == '8':
                operation_user()
            elif choice == '0':
                print("退出程序")
                break
            else:
                print("无效输入，请重新输入")


    # import hashlib
    #
    # conn = sqlite3.connect('database.db')
    # c = conn.cursor()
    #
    # # 创建用户表
    # def create_user_table():
    #     c.execute('''CREATE TABLE IF NOT EXISTS users (
    #                     id INTEGER PRIMARY KEY,
    #                     username TEXT NOT NULL UNIQUE,
    #                     password TEXT NOT NULL
    #                 )''')
    #     conn.commit()
    #
    # # 查询整个用户表
    # def query_all_users():
    #     c.execute("SELECT * FROM users")
    #     users = c.fetchall()
    #     for user in users:
    #         print(user)
    #
    # # 查询特定用户
    # def query_user_by_id():
    #     user_id = input("请输入要查询的用户ID: ")
    #     c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    #     user = c.fetchone()
    #     if user:
    #         print(user)
    #     else:
    #         print("未找到该用户")
    #
    # # 插入用户
    # def insert_user():
    #     username = input("请输入用户名: ")
    #     password = input("请输入密码: ")
    #     hashed_password = hashlib.sha256(password.encode()).hexdigest()
    #     try:
    #         c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    #         conn.commit()
    #         print("用户添加成功！")
    #     except sqlite3.IntegrityError:
    #         print("用户名已存在，请选择其他用户名。")
    #
    # # 更新用户密码
    # def update_user_password():
    #     user_id = input("请输入要更新密码的用户ID: ")
    #     new_password = input("请输入新密码: ")
    #     hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    #     c.execute("UPDATE users SET password=? WHERE id=?", (hashed_password, user_id))
    #     conn.commit()
    #     print("密码更新成功！")
    #
    # # 删除用户
    # def delete_user_by_id():
    #     user_id = input("请输入要删除的用户ID: ")
    #     c.execute("DELETE FROM users WHERE id=?", (user_id,))
    #     conn.commit()
    #     print("用户删除成功！")
    #
    # # 创建数据表
    # def create_tables():
    #     create_user_table()
    #
    # # 主菜单
    # def main_menu():
    #     while True:
    #         print("1. 查询用户表")
    #         print("2. 查询特定用户")
    #         print("3. 添加用户")
    #         print("4. 更新用户密码")
    #         print("5. 删除用户")
    #         print("0. 退出程序")
    #
    #         choice = input("请输入选项: ")
    #
    #         if choice == '1':
    #             query_all_users()
    #         elif choice == '2':
    #             query_user_by_id()
    #         elif choice == '3':
    #             insert_user()
    #         elif choice == '4':
    #             update_user_password()
    #         elif choice == '5':
    #             delete_user_by_id()
    #         elif choice == '0':
    #             print("退出程序")
    #             break
    #         else:
    #             print("无效输入，请重新输入")

# if __name__ == '__main__':
#     create_tables()
#     main_menu()

def create_tables():
    # 在这里编写创建数据库表格的代码
    pass

if __name__ == '__main__':
    app = CinemaManagementSystem()
    create_tables()  # 调用创建数据库表格的函数
    start_server(app.main, port=8080)
