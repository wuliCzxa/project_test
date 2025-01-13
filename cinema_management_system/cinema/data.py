# data.py

import sqlite3
import pandas as pd
import shutil
import hashlib

# 创建数据表函数
def create_tables():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

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

    # 创建用户表
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()

# 插入数据函数
def insert_data():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

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

# 插入电影信息的函数
def insert_movies():
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
        genre = input("请输入类型：")
        release_date = input("请输入上映时间：")
        duration = input("请输入电影时长：")
        cursor.execute('INSERT INTO movies (movie_id, movie_name,director,cast,genre,release_date,duration) VALUES (?, ?, ?, ?, ?, ?, ?)', (movie_id, movie_name,director,cast,genre,release_date,duration))
    else:
        print("无效的选择，请重新选择。")

    conn.commit()
    print("电影信息已插入")
    conn.close()

# 插入顾客信息的函数
def insert_customers():
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
        gender = input("请输入顾客性别: ")
        age = int(input("请输入顾客年龄: "))
        phone = input("请输入顾客电话: ")
        email = input("请输入顾客邮箱: ")
        cursor.execute('INSERT INTO customers (customer_id, name,gender,age,phone,email) VALUES (?, ?, ?, ?, ?, ?)', (customer_id, name,gender,age,phone,email))
    else:
        print("无效的选择，请重新选择。")

    conn.commit()
    print("顾客信息已插入")
    conn.close()

# 插入影票信息的函数
def insert_tickets():
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
        screening_id = int(input("请输入放映ID: "))
        seat_number = input("请输入座位号: ")
        price = float(input("请输入票价: "))
        cursor.execute('INSERT INTO tickets (ticket_id, movie_id, customer_id,screening_id,seat_number,price) VALUES (?, ?, ?, ?, ?, ?)', (ticket_id, movie_id, customer_id,screening_id,seat_number,price))
    else:
        print("无效的选择，请重新选择。")

    conn.commit()
    print("影票信息已插入")
    conn.close()

# 插入放映信息的函数
def insert_screenings():
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

# 查询数据函数
def query_data():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

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

    conn.close()

# 查询电影信息的函数
def query_movies():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    print("\n电影信息：")
    for movie in movies:
        print(movie)

    conn.close()

# 查询顾客信息的函数
def query_customers():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    print("\n顾客信息：")
    for customer in customers:
        print(customer)

    conn.close()

# 查询影票信息的函数
def query_tickets():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tickets')
    tickets = cursor.fetchall()
    print("\n影票信息：")
    for ticket in tickets:
        print(ticket)

    conn.close()

# 查询放映信息的函数
def query_screenings():
    conn = sqlite3.connect('电影院管理系统.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM screenings')
    screenings = cursor.fetchall()
    print("\n放映信息：")
    for screening in screenings:
        print(screening)

    conn.close()

# 按电影ID查询电影信息的函数
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

# 按顾客ID查询顾客信息的函数
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

# 按影票ID查询影票信息的函数
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

# 按放映ID查询放映信息的函数
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

# 更新数据函数
def update_data():
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

# 更新电影信息的函数
def update_movies():
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

# 更新顾客信息的函数
def update_customers():
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

# 更新影票信息的函数
def update_tickets():
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

# 更新放映信息的函数
def update_screenings():
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

# 删除数据函数
def delete_data():
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


# 删除电影信息的函数
def delete_movies():
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


# 删除顾客信息的函数
def delete_customers():
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


# 删除影票信息的函数
def delete_tickets():
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


# 删除放映信息的函数
def delete_screenings():
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


# 备份数据函数
def backup_data():
    # 备份数据库文件
    shutil.copyfile('电影院管理系统.db', '电影院管理系统_backup.db')
    print("数据库备份完成")


# 用户注册函数
def register_user():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 对密码进行哈希处理
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 尝试插入新用户信息到数据库
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("注册成功！")
    except sqlite3.IntegrityError:
        print("用户名已存在，请选择其他用户名。")

    conn.close()

# 用户登录函数
def login_user():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 对密码进行哈希处理
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 查询数据库中是否存在匹配的用户名和密码
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        print("登录成功！")
    else:
        print("用户名或密码错误。")

    conn.close()
