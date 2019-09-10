# pip list 可以显示 已安装的库
# 查看所有的库及其中的内容 网页文档，可以用 python -m pydoc -p 0

from static.simple_class import A
from static import simple_class
import math.inf as oo
import math


# 使用 dir 可查看包內的內容
print(dir(math))
print(dir(simple_class))
print(dir(simple_class.A))

# python3 中设置 path 的方法没有成功导入包
# import sys
# sys.path.append("./static/")
# python3 以点开头可表示相对路径 需要保证在索引过程中目录中始终存在 __init__.py
# 这种方法只能作为模块调用，且不能达到最顶层
# py -3 -m small_code.simple_py.07_import
# print(__name__,__package__)
# from .. import shiyanlou
# print(dir(shiyanlou))


# 使用 hasattr 判断是否有某个方法/成员
print(hasattr(simple_class.A, "foo"))

# vars([object]) 返回object对象的__dict__属性
# 对象必须有 __dict__ 方法
print(vars(A))

# help([object])调用内置帮助系统
print(help(A))

# callable() 函数，对象是否是可调用的
a = A()
print(callable(a))
print(callable(A))
print(callable(A.foo))
