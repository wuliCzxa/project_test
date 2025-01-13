# from flask import Flask, render_template, request, redirect, url_for, session
# import sqlite3
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
#
# # 连接数据库
# conn = sqlite3.connect('data.py')
# cursor = conn.cursor()
#
# # 用户注册
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # 插入用户信息到数据库
#         cursor.execute("INSERT INTO customers (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         return redirect(url_for('login'))
#     return render_template('register.html')
#
# # 用户登录
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # 查询数据库中是否存在该用户
#         cursor.execute("SELECT * FROM customers WHERE username = ? AND password = ?", (username, password))
#         user = cursor.fetchone()
#         if user:
#             session['username'] = username
#             return redirect(url_for('user_page'))
#         else:
#             return 'Invalid username or password'
#     return render_template('login.html')
#
# # 用户主页
# @app.route('/user_page')
# def user_page():
#     if 'username' in session:
#         return render_template('users.html')
#     return redirect(url_for('login'))
#
# # 电影列表页
# @app.route('/movies')
# def movies():
#     if 'username' in session:
#         # 查询数据库获取电影列表
#         cursor.execute("SELECT * FROM movies")
#         movie_list = cursor.fetchall()
#         return render_template('movies.html', movies=movie_list)
#     return redirect(url_for('login'))
#
# # 电影详情页
# @app.route('/movie/<int:movie_id>')
# def movie_detail(movie_id):
#     if 'username' in session:
#         # 查询数据库获取电影详情
#         cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
#         movie = cursor.fetchone()
#         return render_template('movie_detail.html', movie=movie)
#     return redirect(url_for('login'))
#
# # 退出登录
# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import pandas as pd
import shutil

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置一个密钥用于session加密
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///电影院管理系统.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect('/')
        return render_template('login.html', error='用户名或密码错误')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not User.query.filter_by(username=username).first():
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        return render_template('register.html', error='用户名已被占用')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/query_data')
def query_data():
    # 实现查询数据的函数
    return render_template('query_data.html')

# 实现其他数据库操作的函数

if __name__ == '__main__':
    app.run(debug=True)
    #create_tables()
    query_data()


