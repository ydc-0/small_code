import numpy
import random

# numpy random
array1 = numpy.random.rand(2)
print(array1)  # [0.37120327 0.64113004]
array1 = numpy.random.randint(0, 9, size=5)  # [min, max) -> 0~8
print(array1)
array1 = numpy.random.randint(0, 10, size=(2, 5))
print(array1)
array1 = numpy.random.randint(0, 10, size=(2, 3, 4))  # 多维数组
# print(array1)

# random
array1 = [1, 2, 3, 4, 5]
random.shuffle(array1)  # shuffle 打乱原序列
print(array1)
array1 = [1, 2, 3, 4, 5]
rad = random.choice(array1)
print(rad)
print(random.uniform(1, 3))  # 浮点数

state = random.getstate()
print(random.randint(0, 9))
random.setstate(state)
print(random.randint(0, 9))  # same state -> same result

# distribution 分布
rad = random.normalvariate(0, 1)  # 正态分布
rad = random.lognormvariate(0, 1)  # 对数高斯分布
rad = random.triangular(0, 1, 0.5)  # 对称分布
rad = random.betavariate(1, 2)  # Bata分布
# ...
array1 = numpy.random.standard_normal(size=10)  # 正态分布序列
# ...


# numpy 是一个运行速度很快的数学库
# numpy 还有很多矩阵运算的方法
# 菜鸟教程 ： https://www.runoob.com/numpy/numpy-tutorial.html
