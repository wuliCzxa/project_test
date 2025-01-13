import sqlite3

# 创建或连接到数据库
conn = sqlite3.connect('/mnt/data/cinema_management_system.db')
cursor = conn.cursor()

# 创建电影信息表
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    movie_name TEXT,
    director TEXT,
    cast TEXT,
    genre TEXT,
    release_date DATE,
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
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(screening_id) REFERENCES screenings(screening_id)
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
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()

"数据库和表已创建。"
# 重新连接到数据库
conn = sqlite3.connect('/mnt/data/cinema_management_system.db')
cursor = conn.cursor()

# 准备模拟数据
movies_data = [
    (1, 'The Lord of the Rings: The Fellowship of the Ring', 'Peter Jackson', 'Elijah Wood, Ian McKellen, Viggo Mortensen', 'Fantasy', '2001-12-19', 178),
    (2, 'The Dark Knight', 'Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart', 'Action', '2008-07-18', 152)
]

customers_data = [
    (1, 'Alice', 'Female', 25, '1234567890', 'alice@email.com'),
    (2, 'Bob', 'Male', 30, '0987654321', 'bob@email.com')
]

tickets_data = [
    (1, 1, 1, 1, 'A1', 100.0),
    (2, 1, 2, 1, 'A2', 100.0)
]

screenings_data = [
    (1, 1, 'Room 1', '2024-04-21 20:00', 'Not screened yet'),
    (2, 2, 'Room 2', '2024-04-22 18:00', 'Not screened yet')
]

# 插入数据到电影信息表
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?)', movies_data)

# 插入数据到顾客信息表
cursor.executemany('INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)', customers_data)

# 插入数据到影票信息表
cursor.executemany('INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?)', tickets_data)

# 插入数据到放映信息表
cursor.executemany('INSERT INTO screenings VALUES (?, ?, ?, ?, ?)', screenings_data)

# 提交更改并关闭连接
conn.commit()
conn.close()

"已插入模拟数据到数据库中。"

