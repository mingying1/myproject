#定义一个天山童姥类 ，类名为TongLao
class TongLao:
    #定义童姥的属性 属性有血量，武力值（通过传入的参数得到）
    #构造方法
    def __init__(self,tl_hp,tl_power):
        self.tl_hp = tl_hp
        self.tl_power = tl_power
    #定义童姥see_people的方法 需要传入一个name参数
    def see_people(self,name):
        self.name = name
        #如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if self.name == "WYZ":
            print("师弟!!!!")
        #如果传入“李秋水”，打印“呸，贱人”，
        elif self.name == "李秋水":
            print("呸，贱人")
        #如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")

        #fight_zms方法（天山折梅手）调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    def fight_zms(self,t_hp,t_power,your_hp,your_power):
        self.t_hp = self.tl_hp/2
        self.t_power = self.tl_power*10

        #需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
        self.your_hp = your_hp
        self.your_power = your_power
        #童姥使用折梅手的血量 = 童姥使用折梅手的血量 - 你的攻击力
        self.t_hp = self.t_hp - your_power
        # 你的血量 = 你的血量 - 童姥使用折梅手的攻击力
        self.your_hp = your_hp - self.t_power
        #比较双方血量。血多的一方获胜。
        if self.t_hp > self.your_hp:
            print("果然是童姥的折梅手厉害")
        elif self.t_hp < self.your_hp:
            print("童姥的折梅手也不过如此")
#定义一个XuZhu类，继承于童姥。
class XuZhu(TongLao):
#虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    def __init__(self,read):
        print(f"{read}罪过罪过")
tl = TongLao(1000,100)
tl.see_people("李秋水")
tl.fight_zms(1000,100,1000,100)
xz = XuZhu("念经:")






