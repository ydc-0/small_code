# coding=utf-8


k = 10

# 一行代码输出斐波那契数列
print([x[0] for x in [(a[i], a.append(a[-1]+a[-2])) for a in [[1,1]] for i in range(k)]])
# print([(a[i], a.append(a[-1]+a[-2])) for a in [[1,1]] for i in range(k)])


# 通项公式：
# Fn = (pow((1+sqrt(5))/2,n)-pow((1-sqrt(5))/2,n))/sqrt(5)
# 斐波那契数列通项公式是怎样推导出来的？ - Daniel Xiang的回答 - 知乎
# https://www.zhihu.com/question/25217301/answer/158291644



# 初中生的推导方式： 
# TODO： why wrong

from math import sqrt


a = 5.0
b = 3.0
c = 2.0
C = 1.0
D = 2.0


def func(i):
    if i == 0:
        return C
    elif i == 1:
        return D
    else:
        return a * func(i - 1) + b * func(i - 2) + c


print(func(k))

a1 = (a + sqrt(a * a + 4.0 * b)) / 2.0
# a1 = (a - sqrt(a * a - 4 * b))/2.0
t = a1 - a
Y1 = D + t * C
# YN = pow(a1,k) * (Y1 + c/(a1-1))/a1 - c/(a1-1)
aa = -t
bb = (Y1 + c/(a1-1.0))/a1
bb1 = a1
cc = c/(a1-1.0)

e = cc/(aa-1.0)
t1 = (bb * bb1)/(aa-bb1)
X0 = C + e + t1
XN = pow(aa, k) * X0
ZN = XN - t1 * pow(bb1, k) - e
print(ZN)
exit(0)


