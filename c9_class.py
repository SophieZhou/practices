# -*- coding: utf-8 -*-


class Person3: 
   
    def __init__(self, name,age): #构造函数
        self.name = name #把参数name赋值给self.name，即成员变量name（域）
        self.age = age    #把参数age赋值给self.age，即成员变量age（域）
       
    def __del__(self):        #析构函数
        print('__del__()被调用',self.name)
        
    def say_hi(self):        #定义类Person3的方法say_hi()
        print('您好, 我叫', self.name)
   
p31 = Person3('张',25)    #创建对象
p31.say_hi()        #调用对象的方法
p32 = Person3('李',28)   #创建对象
p32.say_hi()        #调用对象的方法




class Point: 
    def __init__(self, x = 0, y = 0): #构造函数
        self.x = x 
        self.y = y 
p1 = Point()                   #创建对象
print("p1({0},{1})".format(p1.x, p1.y))
p1 = Point(5, 5)               #创建对象
print("p1({0},{1})".format(p1.x, p1.y))



class Person:             #定义类Person
    def __init__(self, name): #__init__方法
        self.name = name #把参数name赋值给self.name，即成员变量name（域）
    def say_hi(self):     #定义类Person的方法say_hi
        print('您好, 我叫', self.name)
p5 = Person('Helen')    #创建对象
p5.say_hi()            #调用对象的方法


class Dog(): 
    #程序会自动运行__init__（）创建实例
    def __init__(self,name,age): 
        self.name = name  # 属性
        self.age = age
       
        #方法
    def sit(self):
        print(self.name.title()+' is now sitting.')
    
    def roll_over(self):
        print(self.name.title()+' rolled over!')

# #当使用print输出对象时，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    # def __str__(self):
    #     return ('The dog\'s name is {}.').format(self.name)

my_dog = Dog('Tommy',8)
my_dog.sit()
your_dog = Dog('Willie',6)
your_dog.roll_over()
print(my_dog)


class Test:
    @classmethod
    def f1(cls, info):
        print(info)

    @staticmethod
    def f2(info):
        print(info)
 
Test.f1('hi')
Test.f2('hello')
t = Test()
t.f1('hi')
t.f2('hello')



class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year)+' ' + self.make + ' ' + self.model
        return long_name
    
    def update_odometer(self,mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer.')

    def read_odometer(self):
        print('This car hs ' + str(self.odometer_reading) + ' miles on it.')
        
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        print('Please fill gas into the gas tank.')
        
my_tesla = Car('tesla','model s',2016)
my_tesla.odometer_reading = 23    
my_tesla.read_odometer()

        
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
        
    def describe_battery(self):
        print('This car has a '+ str(self.battery_size)+'-kwh battery.')
        
    def fill_gas_tank(self):
        print('This car does not need a gas tank.')
        
if __name__=='__main__':
    my_tesla = ElectricCar('tesla','model s',2016)
    my_tesla.odometer_reading = 23    
    my_tesla.read_odometer()
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    my_tesla.fill_gas_tank()


class Person:                 #基类
    def __init__(self, name, age): #构造函数
        self.name = name     #姓名
        self.age = age        #年龄
        
    def say_hi(self):         #定义基类方法say_hi
        print('您好, 我叫{0}, {1}岁了'.format(self.name,self.age))
        
    def incre_age(self,years):
        self.age += years
        
    def update_age(self,age):
        self.age = age
        print('{}现在的年龄是{}'.format(self.name,self.age))
        
        
class Student(Person):         #派生类
    def __init__(self, name, age, stu_id,grade): #构造函数
        super().__init__(name,age)
#        Person.__init__(self, name, age) #调用基类构造函数
        self.stu_id = stu_id    #学号
        self.grade = grade
        
    def say_hi(self):          #定义派生类方法say_hi
        super().say_hi()    #调用基类方法say_hi
        print('我是学生{}, 我的学号为：{}'.format(self.name, self.stu_id))
        
    def update_age(self,age): 
        self.age = age
        if age>=18:
            print('学号为{}的学生现在年龄是{}'.format(self.stu_id,self.age))
        else:
            print('学号为{}的学生是未成年，应该在少年班。'.format(self.stu_id))
     
    def get_grade(self):
        print('学号为{}的学生，成绩为{}.'.format(self.stu_id,self.grade))

if __name__=='__main__':
    p1 = Person('张王一', 33)            #创建对象
    p1.say_hi()
    p1.update_age(20) 
    p1.age = 26
    p1.incre_age(6)
    p1.say_hi()
    
    s1 = Student('李姚二', 20, '2018101001',90) #创建对象
    s1.say_hi()
    s1.get_grade()
    s1.update_age(16)


class Dimension:  #定义类Dimensions
    def __init__(self, x, y): #构造函数
        self.x = x       #x坐标
        self.y = y       #y坐标
        
    def area(self):       #基类的方法area()
        pass
        
class Circle(Dimension):  #定义类Circle（圆）
    def __init__(self, r): #构造函数
         super().__init__( r, 0)  # Dimension.__init__(self,r,0)
         
    def area(self):        #覆盖基类的方法area()
        return 3.14 * self.x * self.x   #计算圆面积
        
class Rectangle(Dimension):  #定义类Rectangle（矩形）
    def __init__(self, w, h): #构造函数
        super().__init__(w, h)
        
    def area(self):  #覆盖基类的方法area()
        return self.x * self.y  #计算矩形面积
        
d1 = Circle(2.0)          #创建对象：圆
d2 = Rectangle(2.0, 4.0)   #创建对象：矩形
print(d1.area(), d2.area())  #计算并打印圆和矩形面积
