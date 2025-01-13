#
# from test_function import judge_season, register_login, calculate, total_scores
#
# def main():
#
#     while True:
#
#         print("1. 判断季节")
#         print("2. 注册登录")
#         print("3. 计算序列和")
#         print("4. 统计学生成绩并保存总分")
#         print("0. 退出")
#
#         choice = input("请输入选项（0-4）：")
#
#         if choice == "1":
#             month = int(input("请输入月份（1-12）："))
#             season = judge_season(month)
#             print(f"{month}月为{season}季的三个月份之一\n")
#         elif choice == "2":
#             register_login()
#         elif choice == "3":
#             n = int(input("请输入一个整数n："))
#             result = calculate(n)
#             print(f"奇偶计算结果为：{result}\n")
#         elif choice == "4":
#             total_scores()
#             print("学生总分已保存到demo_total.txt文件。\n")
#         elif choice == "0":
#             print("退出程序\n")
#             break
#         else:
#             print("无效的选项，请重新输入！\n")
#
# if __name__ == "__main__":
#     main()
x=100
def func():
    print(x)