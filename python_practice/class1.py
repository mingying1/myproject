#定义一个类
class Person:
    #定义类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0
    #构造方法 在类实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        #self.变量名的方式,访问的问题,叫做实例变量名
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    #定义类方法
    def eat(self):
        print(f"{self.name} eating")

    def play(self):
        print(f"{self.name}playing")

    def jump(self):
        print(f"{self.name}jump")

    #类的实例化 创建一个实例

zs = Person('zhangsan',20,'男',130)
zs.eat()
print(f"zhangsan的姓名是:{zs.name},张山的年龄是:{zs.age},zhangsan的性别是:{zs.gender}")

