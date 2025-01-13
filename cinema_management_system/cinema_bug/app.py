# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
# import hashlib
# import os
#
# app = Flask(__name__)
#
# # 数据库文件路径
# DATABASE = os.path.join(os.path.dirname(__file__), 'data.py')
#
# # 连接到数据库
# def connect_db():
#     return sqlite3.connect(DATABASE)
#
# # 主页路由
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # 用户注册路由
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         conn = connect_db()
#         cursor = conn.cursor()
#
#         # 对密码进行哈希处理
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         # 尝试插入新用户信息到数据库
#         try:
#             cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
#             conn.commit()
#             return redirect(url_for('login'))
#         except sqlite3.IntegrityError:
#             error = "用户名已存在，请选择其他用户名。"
#             return render_template('register.html', error=error)
#
#         conn.close()
#
#     return render_template('register.html')
#
# # 用户登录路由
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         conn = connect_db()
#         cursor = conn.cursor()
#
#         # 对密码进行哈希处理
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#
#         # 查询数据库中是否存在匹配的用户名和密码
#         cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
#         user = cursor.fetchone()
#
#         if user:
#             return redirect(url_for('user'))
#         else:
#             error = "用户名或密码错误。"
#             return render_template('login.html', error=error)
#
#         conn.close()
#
#     return render_template('login.html')
#
# # 用户主页路由
# @app.route('/user')
# def user():
#     return render_template('user.html')
#
# # 电影列表路由
# @app.route('/movies')
# def movies():
#     conn = connect_db()
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT * FROM movies")
#     movies = cursor.fetchall()
#
#     conn.close()
#
#     return render_template('movies.html', movies=movies)
#
# # 电影详情路由
# @app.route('/movie/<int:movie_id>')
# def movie_detail(movie_id):
#     conn = connect_db()
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT * FROM movies WHERE movie_id=?", (movie_id,))
#     movie = cursor.fetchone()
#
#     conn.close()
#
#     return render_template('movie_detail.html', movie=movie)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from pywebio.input import input, PASSWORD, TEXT
from pywebio.output import put_text, put_markdown
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import hashlib
import sqlite3

# Create Flask app
app = Flask(__name__)

# Database file path
DATABASE = 'data.db'

# User registration function
def register(username, password):
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert new user information into the database
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        put_text("Registration successful!")
    except sqlite3.IntegrityError:
        put_text("Username already exists. Please choose another username.")

    # Close the database connection
    conn.close()

# User login function
def login(username, password):
    # Connect to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and password match in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        put_text("Login successful!")
    else:
        put_text("Username or password incorrect.")

    # Close the database connection
    conn.close()

# Flask route for PyWebIO app
@app.route('/')
def index():
    return "PyWebIO app is running!"

# Flask route for the login and registration forms
@app.route('/login_register')
def login_register():
    put_markdown('# User Registration and Login')
    username = input("Username:", type=TEXT)
    password = input("Password:", type=PASSWORD)
    login_button = input(" ", type=TEXT, placeholder="Login", validate=lambda x: login(username.value, password.value))
    register_button = input(" ", type=TEXT, placeholder="Register", validate=lambda x: register(username.value, password.value))
    return ""

# Flask route for serving static files
@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory(STATIC_PATH, path)

# Start PyWebIO server as a Flask app
if __name__ == '__main__':
    from pywebio.platform.flask import webio_view
    from pywebio import start_server

    app.add_url_rule('/login_register', 'webio_view', webio_view(login_register), methods=['GET', 'POST'])
    app.run(host='localhost', port=8080)
