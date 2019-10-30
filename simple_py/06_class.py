class A(object):
    def __init__(self, a):
        self.name = "A"
        self.a = a

    def get_a(self):
        return self.a

    def get_name(self):
        return "A"


class B(A):
    def __init__(self, a, b):
        # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
        # python 2 中的super 只支持新类 （object， 即A要继承于 object）
        super().__init__(a)
        # super(B,self).__init__(a)
        # 等同于可用下面的写法
        # A.__init__(self,a)
        # 它们的区别: https://blog.csdn.net/zzhongcy/article/details/41827819
        self.b = b

    def get_b(self):
        return self.b

    def get_name(self):
        return "B"


a1 = A(1)
b1 = B(1, 2)
print(a1.get_a(), a1.get_name())
print(b1.get_a(), b1.get_name())


# 多继承
class A1(object):
    def __init__(self):
        print("-> init A1")
        pass


class A2(object):
    def __init__(self):
        print("-> init A2")
        pass


class A3(A1, A2):
    def __init__(self):
        print("-> init A3")
        super().__init__()


print(A3.__mro__)
a3 = A3()
# (<class '__main__.A3'>, <class '__main__.A1'>, <class '__main__.A2'>, <class 'object'>)
# -> init A3
# -> init A1
# 广度优先，调用第一个找到的符合条件的方法

# TODO：多继承，在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。


# 类的全局变量
class C1:
    # num1 = None
    def __init__(self, num1):
        C1.num1 = num1


class C2:
    # num2 = None
    def __init__(self, num2):
        C2.num2 = num2


class C3(C1, C2):
    def __init__(self):
        pass

    def num(self):
        return C2.num2 + C1.num1


a = C1(2)
b = C2(5)
c = C3()
print(C1.num1, C2.num2, c.num())


# 伪： 私有成语与保护成员
# 单下划线保护成员，双下划线私有成员
# 单下划线命名的变量（包括类，函数，普通变量）不能通过from module import *导入到另外一个模块中。
class E():
    def __init__(self):
        self.__name = 'private name'  # 私有变量，翻译成 self._E__name='python'

    def __say(self):  # 私有方法,翻译成 def _E__say(self)
        print(self.__name)  # 翻译成 self._E__name


a = E()
# print(a.__name) #访问私有属性,报错!AttributeError: E instance has no attribute '__name'
print(a.__dict__)  # 查询出实例a的属性的集合 {'_E__name': 'private name'}
print(a._E__name)  # 这样，就可以访问私有变量了
# a.__say()#调用私有方法，报错。AttributeError: E instance has no attribute '__say'
print(dir(a))  # 获取实例的所有属性和方法
a._E__say()  # 这样，就可以调用私有方法了


# Note:
# __slots__可以控制类成员变量的增加，只有出现在__slots__中的变量才可以增加到类中。
class Foo():
    __slots__ = ('name', 'age')

    def __init__(self, a, b):
        self.name = a
        self.age = 19
        # self.addr = "addr"  # 创建成员时会报错
