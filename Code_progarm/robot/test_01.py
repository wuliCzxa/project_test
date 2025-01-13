from wlkata_mirobot_Virtual import Virtual_WlkataMirobot
import time

# 抓取上方点
P1 = [-51.0, -5.9, 24.7, 0.0, -24.5, -1.4]

# 抓取点
P2 = [-51.0, -4.6, 31.5, 0.0, -28.9, -1.4]

P3 = [0, 2.0, -2.4, 0, -0.9, -1.4]

# 皮带放置点
P4 = [0, 4.8, 17.7, 0, -23.8, -1.4]

# 四轴抓取点 -4
P5 = [-82.4,22.3,73.9,0.0,0,0]

# 四轴抓取点上方 -4
P6=[-82.4,-20.0,-0.6,0.0,0,0]


P7=[-124.3,33.8,62.3,0.0,0,0]

#S上方
P8=[-128.0,-5.6,2.6,0.0,0,0]
arm = Virtual_WlkataMirobot(server_IP="172.22.16.1", server_port=5478)

count = 0

# 机器人复位
arm.home(com1=True)
arm.home(com2=True)

# 皮带线转动
arm.set_Output(2, 1)
arm.set_Output(1, 0)

time.sleep(1)

arm.set_Output(1,1)

time.sleep(2)

#机器人到物料抓取上方
arm.set_joint_angle(com1_P = P1, speed=5000)

#机器人到物料抓取位置
arm.set_joint_angle(com1_P = P2, speed=5000)

#机器人打开吸盘
arm.set_Output(0,1)

#延时，等待吸盘吸附物料
time.sleep(1)
arm.set_joint_angle(com1_P = P1, speed=5000)

#机器人到皮带上方
arm.set_joint_angle(com1_P = P3, speed=5000)

#机器人将物料放置在皮带上
arm.set_joint_angle(com1_P = P4, speed=5000)

#机器人关闭吸盘
arm.set_Output(0,0)

arm.set_Output(2,1)

arm.set_joint_angle(com1_P = P3, speed=5000)

time.sleep(7)

arm.set_Output(2,0)

arm.angles_7_com2=0

#四轴移动到抓取上方
arm. set_joint_angle(com2_P = P6, speed=5000)

#四轴移动到抓取
arm. set_joint_angle(com2_P = P5, speed=5000)

#机器人打开吸盘
time.sleep(3)

arm.set_Output(3,1)

#四轴移动到抓取上方
arm.set_joint_angle(com2_P = P8, speed=5000)
#四轴移动到抓取
arm.set_joint_angle(com2_P = P7, speed=5000)
#机器人关闭吸盘
time.sleep(2)

arm.set_Output(3,0)

time.sleep(4)
#四轴移动到抓取上方
arm.set_joint_angle(com2_P = P8, speed=5000)
time.sleep(1)
arm.set_joint_angle(com2_P = P6, speed=5000)
        