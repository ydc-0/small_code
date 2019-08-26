# coding=utf-8

# y(n) = a * y(n-1) + b * n + c
# y(0) = C
# ---->
# x(n) = y(n) + t * n + e
# x(n) = a * x(n-1)
# x(n) = a^n * x(0)
# x(0) = y(0) + e


k = 5

a = 2.0
b = 1.0
c = 1.0
C = 1.0
def func1(i):
    if i == 0:
        return C
    else:
        return a * func1(i-1) + b * i + c


print(func1(k))
t = b/(a-1)
e = (c + a*t)/(a-1)
X0 = C + e
XN = pow(a,k) * X0
ZN = XN - t * k - e
print(ZN)


# array 2
# y(n) = a * y(n-1) + b * b1 ^ n + c

k = 5

a = 3.0
b = 1.0
c = 1.0
b1 = 2.0
C = 1.0
def func2(i):
    if i == 0:
        return C
    else:
        return a * func2(i-1) + b * pow(b1, i) + c


print(func2(k))
e = c/(a-1)
t = (b * b1)/(a-b1)
X0 = C + e + t
XN = pow(a,k) * X0
ZN = XN - t * pow(b1, k) - e
print(ZN)

exit(0)