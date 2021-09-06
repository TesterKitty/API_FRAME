#类和实例
class Student(object):
    def __init__(self, name, score): #通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart.name)
bart.print_score()
print(bart.get_grade())
#__xx 私有变量名
#变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
#一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#练习：请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender=gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')


def run_twice(a):
    a.run()
    a.run()
#调用同一个函数run_twice(), 传入不同的参数（对象），可以达成不同的功能
run_twice(Animal())
run_twice(Dog())
