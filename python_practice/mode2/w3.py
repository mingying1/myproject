from python_practice.mode.w2 import TongLao

class XuZhu(TongLao):
    # 虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    def read(self):
        print(" 罪过罪过")

    def __init__(self):
        self.read()


tl = TongLao(1000, 100)
tl.see_people("李秋水")
tl.fight_zms(1000, 100, 1000, 100)
xz = XuZhu()