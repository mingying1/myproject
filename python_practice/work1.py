"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

"""
#1,定义一个Dog类
class Dog:
    #定义类的属性
    name = "多多"
    breed = "泰迪"
    gender = "雌性"
    #定义类的方法
    def eat(self):
        print("能吃")
    def pick_up(self):
        print("能捡球")
#打印dog的属性
print(Dog.name,Dog.breed,Dog.gender)
#实例化类
dd = Dog()
#打印类方法
dd.pick_up(),dd.eat()


#2,定义郭德纲,身高,体重,  说相声,演戏
#定义一个GuoDeGang类
class GuoDeGang:
    #定义类的属性
    height = '175cm'
    weight = '85kg'
    #定义类的方法
    def crosstalk(self):
        print("相声界的一哥")
    def acting(self):
        print("演的戏确实不咋滴")
#打印类属性
print(GuoDeGang.height,GuoDeGang.weight)
#实例化类
gdg = GuoDeGang()
#打印类方法
gdg.crosstalk(),gdg.acting()

#3,定义郭麒麟,年龄,性别,  唱歌,继承郭德纲说相声
class GuoQiLin(GuoDeGang):
    #定义类的属性
    age = '24'
    gender = 'male'
    #构造方法
    def __init__(self):
        #调用郭德纲的相声方法
        super().crosstalk()
    #定义类的方法
    def sing(self):
        print("唱歌好听")
#打印类属性
print(GuoQiLin.age,GuoQiLin.gender)
#实例化类
gql = GuoQiLin()
#打印类方法
gql.sing()

#4,创建一个动物类 他要吃,喝 方法;吃进什么,喝进什么,都要输出动物吃了什么,动物喝了什么;
class Zoon:
    #定义吃的方法,传一个食物的参数,打印出传入的食物参数
    def eat(self,food):
        self.food = food
        print(f"动物吃了:{self.food}")

    # 定义喝的方法,传一个饮料的参数,打印出传入的饮料参数
    def drink(self,drinks):
        self.drinks = drinks
        print(f"动物喝了:{self.drinks}")
#实例化类
z = Zoon()
#打印类吃的方法
z.eat("草"),z.drink('water')


#5,创建一个pig类,继承动物类,pig有自己的方法,睡觉
class Pig(Zoon):
    def sleep(self):
        print("爱睡觉")

#实例化类
p = Pig()
#打印类睡觉方法
p.sleep()




