"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_final_hp = my_hp - your_power
your_final_hp = your_hp - my_power
谁的hp先为0，那么谁就输了

"""
# 定义一个 fight 的函数
def fight():
# 定义4个变量 我的血量 我的攻击力 你的血量 你的攻击力
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 200
# 多轮回合下 谁的血量小于等于0 谁就输了
    while True:
        #我的血量=我的血量-你的攻击力
        my_hp = my_hp - your_power
        #你的血量=你的血量-我的攻击力
        your_hp = your_hp - my_power
        #如果我的血量小于等于0 输出 我输了
        if my_hp <= 0 :
            print("我输了")
            #跳出循环
            break
            #如果你的血量小于等于0 输出 你输了
        elif your_hp <=0 :
            print("你输了")
            # 跳出循环
            break
#调用 fight 函数
fight()
