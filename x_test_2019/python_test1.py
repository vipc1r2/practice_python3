#
# class Foo:
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = Foo('cr',24)
# obj1.detail()
#
# obj2=Foo('python',99)
# obj2.detail()
# # Python默认会将obj2传给self参数，即：obj1.detail(obj2)，所以，此时方法内部的 self ＝ obj2，即：self.name 是 python ； self.age 是 99

class Person():
    def __init__(self,name=None,age=None,sex=None):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print("%s正在吃饭"%self.name)

#学生子类：继承人类父类的属性
class Student(Person):
    #子类的初始化参数要和父类的一样，否则没有办法给父类传参，会报错
    def __init__(self,name=None,age=None,sex=None,score=None):
        # self.name=name
        # self.age=age
        # self.sex=sex
        #上面三行的代码等价于下面一行的代码，都是给父类的属性传参
        # Person.__init__(self,name,age,sex)
        #还可以这样写
        super().__init__(name,age,sex)
        self.score=score
    #这个可以是子类独有的方法，不会影响到父类
    def study(self):
        self.eat()
        print("%s在学习，考了%d分"%(self.name,self.score))

    # 方法的重写,调用的时候调用子类的方法
    # 可以对自定义的方法进行重写
    def eat(self):
        print("%d的%s正在吃饭，他是%s的" % (self.age, self.name, self.sex))

    # 也可以对自带的object类的方法进行重写。
    def __str__(self):
        return "姓名：{0}，年龄：{1}，性别：{2}，成绩：{3}".format(self.name, self.age, self.sex, self.score)

    def __lt__(self, other):
        """ if isinstance(other,Student):
            return self.age<other.age
        else:
            return False """
        if self.name == other.name:
            return self.age < other.age
        else:
            return self.name < other.name

# 实例化
stu=Student("汤姆",20,"男",80)
stu.study()
stu.eat()
list1=[]
stu1=Student("杰克",20,"男",90)
stu2=Student("杰森",21,"男",20)
stu3=Student("杰森",12,"女",50)
list1.append(stu)
list1.append(stu1)
list1.append(stu2)
list1.append(stu3)
for student in list1:
    print(student)
list1.sort()
for student in list1:
    print(student)