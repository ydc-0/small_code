# -*- coding: UTF-8 -*-

# python2 不支持中文， 如果文件中有中文，则需要在文件第一行添加 coding: UTF-8
# https://www.python.org/dev/peps/pep-0263/

# 打印数字
a = 1
b = 2
c = a + b
print(c)

# 打印字符串
print("hello world")

# 打印多个元素
print("hello %s" % c)
# print "hello", c  # only in python 2.7
# print("hello", c)  # only in python 3.6

# 打印中文
a = "您好"
print(type(a))
print(a)  # python2.7 命令行中还会乱码
# 命令行可能以 BMK 编码显示
# print(a.decode("utf-8"))  # python2.7 可以使用

a = u"您好"
print(type(a))
print(a)  # python2.7 正常

# python3.6 中以上两种都可以直接print(a), 不会乱码
# python3.6 中两种定义方式都为 str
# python2.7 中 为 str 和 unicode

# 作为一个变量，大部分类型都可以直接使用 print(a) 直接打印，
# 某些情况需要 print(str(a))
a = None
print("a is:", a)
b = [1, 2, 3]
print("b is:", b)
