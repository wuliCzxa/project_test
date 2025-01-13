#春夏秋冬
def judge_season(month):

    if month in [3, 4, 5]:
        return "春"
    elif month in [6, 7, 8]:
        return "夏"
    elif month in [9, 10, 11]:
        return "秋"
    elif month in [12, 1, 2]:
        return "冬"
    else:
        return "输入无效"

#注册or登录
def register_login():

    # 读取
    def load_users():
        users = {}
        try:
            with open('users.txt', 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    username, password = line.strip().split(',')
                    users[username] = password
        except FileNotFoundError:
            pass

        return users

    # 保存
    def save_users(username, password):
        with open('users.txt', 'a', encoding='utf-8') as file:
            file.write(f"{username},{password}\n")

    # 注册
    def register():
        users = load_users()
        name = input("请输入用户名：")
        if name in users:
            print("用户名已存在，注册失败。")
        else:
            password = input("请输入密码：")
            save_users(name, password)
            print("注册成功！")

    # 登录
    def login():
        users = load_users()
        name = input("请输入用户名：")
        password = input("请输入密码：")
        if users.get(name) == password:
            print(f"欢迎{name}登录")
        else:
            print("用户名或密码错误，请重新登录！")

    action = input("请选择操作（1：注册，2：登录）：")
    if action == "1":
        register()
    elif action == "2":
        login()
    else:
        print("无效操作")

#计算
def calculate(n):

    result = 0
    if n % 2 == 0:
        # n为偶
        for i in range(2, n + 1, 2):
            result += 1 / i
    else:
        # n为奇
        for i in range(1, n + 1, 2):
            result += 1 / i

    return result

#统计总分，入新文件
def total_scores():

    with open('demo.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    student_scores = {}

    for line in lines:
        parts = line.split()
        name = parts[0]
        scores = list(map(int, parts[1:]))
        total_score = sum(scores)
        student_scores[name] = total_score

    with open('demo_total.txt', 'w', encoding='utf-8') as f:
        for name, total_score in student_scores.items():
            f.write(f"{name} {total_score}\n")


if __name__ == "__main__":

    # month = int(input("请输入月份（1-12）："))
    # season = judge_season(month)
    # print(f"{month}月为{season}季的三个月份之一\n")
    #
    # register_login()
    #
    # n = int(input("请输入一个整数n："))
    # result = calculate(n)
    # print(f"奇偶计算结果为：{result}\n")
    #
    total_scores()
    print("学生总分已保存到demo_total.txt文件。\n")

