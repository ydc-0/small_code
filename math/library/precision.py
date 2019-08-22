import math
from decimal import Decimal, getcontext, localcontext
import sympy
from fractions import Fraction

# decimal
a = Decimal('0.1')
b = Decimal('0.3')
print(a, b)  # 0.1 0.3
print(a + b)  # 0.4
print(a / b)  # 0.33333333
print(a / b * Decimal('3'))  # 0.99999999
# getcontext().prec = 3
# print(a / b)  # 0.333
# print(a / b * Decimal('3'))  # 0.999
with localcontext() as lc:
    lc.prec = 50
    c = a / b
print(c * Decimal('3'))  # 1.00000000

# math.sum
num_list = [3.21e+18, 1, -3.21e+18]
print(sum(num_list))  # 0.0
print(math.fsum(num_list))  # 1.0

# sympy
print(math.sqrt(8))  # 2.8284271247461903
print(sympy.sqrt(8))  # 2*sqrt(2)
print(type(sympy.Rational(1, 3)))  # <class 'sympy.core.numbers.Rational'>
# sympy symbols
x, y, z = sympy.symbols('x y z')
y = x + 1
expr = x**2 + 2*y
print(expr)  # x**2 + 2*x + 2
print((x+3*z).subs({x: 1, z: 2}))  # 7
print(sympy.Eq(x+1, z))  # Eq(x + 1, z)
print(sympy.Eq(x**3, x*x*x))  # True
# sympy simplify
expr1 = (x+1)**2
expr2 = x**2 + 2*x + 1
print(sympy.Eq(expr1, expr2))  # Eq((x + 1)**2, x**2 + 2*x + 1)
print(sympy.Eq(sympy.simplify(expr1 - expr2), 0))  # True

# Fraction
a = Fraction('0.1')
b = Fraction(2, 3)
c = Fraction('1/3')
print(a + b + c)  # 11/10
