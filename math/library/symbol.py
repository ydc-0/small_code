import sympy
import math
# 同目录的 precision 中也包含了 sympy 的部分用法

# 符号：
x = sympy.symbols('x')
y,z = sympy.symbols('y z')

# 表达式
expr1 = 2 * x - y - 3
expr2 = 3 * x + y - 7

# 解方程 
# expr1 = 0 and expr2 = 0
print(sympy.solve([expr1,expr2], [x,y])) 
# output: {x: 2, y: 1}

# 无穷大 oo
print(sympy.oo > 100, sympy.oo + 1 == sympy.oo)
# output: True True

# 特殊符号： pi，e ... 
# exp(n) = e ^ n
print(sympy.pi, sympy.pi.evalf())
print(sympy.E, sympy.E.evalf())

# 化简 simplify 将尝试多种化简，返回其认为的“最简化”结果
expr = sympy.sin(x)**2 + sympy.cos(x)**2
# 不能使用 math.sin
print(sympy.simplify(expr))
print(sympy.simplify( x+2*x-x-x ))

# 展开表达式 expand
expr = (x + 1)**2
print(sympy.expand(expr))
# 因式分解 factor, factor_list
expr = x**2 + 2*x + 1
print(sympy.factor(expr))
# 合并同类项 collect
expr = x**2 + 2*x + x + 1
print(sympy.collect(expr, x))
# 分式化简 cancel
expr = (x**2 + 2*x + 1)/(x**2 + x)
print(sympy.cancel(expr))
# 分式裂项  apart
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
print(sympy.apart(expr))
# 三角化简 trigsimp
expr = sympy.sin(x) / sympy.cos(x)
print(sympy.trigsimp(expr))
# 三角展开 expand_trig
expr = sympy.sin(x + y)
print(sympy.expand_trig(expr))
# 指数化简 powsimp / 指数展开 expand_power_exp
a,b = sympy.symbols('a b')
expr = x**a*x**b
print(sympy.powsimp(expr))
# 化简指数的指数 powdenest
# 必须满足条件 底数 positive=True
x = sympy.symbols('x', positive=True)
expr = (x**a)**b
print(sympy.powdenest(expr))
# 对数展开 expand_log / 对数合并 logcombine
# 需要指出 log ln 在 sympy 中都是自然对数
# symbol 也需要满足条件
x, y = sympy.symbols('x y', positive=True)
n = sympy.symbols('n', real=True)
print(sympy.expand_log(sympy.log(x**n)))
print(sympy.expand_log(sympy.log(x*y)))

# more: 
# series-泰勒展开函数
# diff-求导
# pprint-将公式用更好看的格式打印出来
sympy.pprint(x/(y+1))
