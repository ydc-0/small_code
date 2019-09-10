import itertools
# itertools 是内置库 https://docs.python.org/2/library/itertools.html
# 主要功能是迭代器和排列组合

# 迭代器 count, cycle, repeat
itertools.count(start=0, step=1)  # 无限迭代，最大值 sys.maxint，下一个 -sys.maxint-1
for d in zip(['a', 'b', 'c'], itertools.count()):
    print(d)

# 多个迭代器变为同一个迭代器：
for c in "AB", "CD":
    print(c)  # AB,CD
for c in itertools.chain("AB", "CD"):
    print(c)  # A,B,C,D

# compress 选择序列
print(list(itertools.compress("ABCD", [0, 1, 1, 0])))  # ['B', 'C']

# dropwhile 丢弃*符合*条件的前几项
it = itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 6, 4, 1])
print(list(it))  # [6, 4, 1]
# filter vs itertools.ifilter -> python 2 中后者返回迭代对象，更省内存， python 3 中可直接使用 filter
print(list(filter(lambda x: x < 5, [1, 2, 3, 6, 4, 1])))  # [1, 2, 3, 4, 1]

# 排列组合
# product 笛卡尔积　　（有放回抽样排列）
# permutations 排列　　（不放回抽样排列）
# combinations 组合,没有重复　　（不放回抽样组合）
# combinations_with_replacement 组合,有重复　　（有放回抽样组合）
array = [1, 2, 3]
print(list(itertools.product(array, repeat=2)))
print(list(itertools.combinations(array, 2)))

# 注： yield 关键字可以把函数转变为
