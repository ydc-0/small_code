import numpy
import numpy.matlib
# if don't import numpy.matlib, exception "module 'numpy' has no attribute 'matlib'" is raised.

print(numpy.matlib.empty((2, 2)))
print(numpy.matlib.zeros((2, 2)))
print(numpy.matlib.ones((2, 2)))
# 注：numpy.matlib 模块中的函数返回的是一个矩阵，而不是 ndarray 对象。

a = numpy.array([[1, 0], [0, 0]])
b = numpy.array([[1, 1], [0, 1]])
print(numpy.dot(a, b))
print(numpy.linalg.det(b))

# numpy.dot         两个数组的点积，即元素对应相乘。
# numpy.vdot        两个向量的点积
# numpy.inner	    两个数组的内积
# numpy.matmul      两个数组的矩阵积
# numpy.linalg.det  计算输入矩阵的行列式
# numpy.linalg.solve 求解线性矩阵方程
# numpy.linalg.inv  计算矩阵的乘法逆矩阵

a1 = numpy.mat([[1, 1], [2, 3], [4, 2]])
print(a1.sum(axis=0))
print(a1.sum(axis=1))
print(numpy.sum(a1, 0))

# 矩阵切割
a1 = numpy.mat(numpy.ones((3, 3)))
print(a1[1:, 1:])

# 注：Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。
