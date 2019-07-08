# 实现不可修改的字典-实验楼
# https://www.shiyanlou.com/challenges/4251/
# 这题有点坑，需要重写 __setitem__ pop popitem update clear __delitem__ setdefault
# 题目要求：执行任何会改变字典数据的方法时，抛出 TypeError 异常
# 不是只有示例中的操作

class ImmutableDict(dict):

    def update(self, __m, **kwargs):
        raise TypeError("'ImmutableDict' objects are immutable")

    def popitem(self):
        raise TypeError("'ImmutableDict' objects are immutable")

    def clear(self):
        raise TypeError("'ImmutableDict' objects are immutable")

    def pop(self, k):
        raise TypeError("'ImmutableDict' objects are immutable")

    def __setitem__(self, k, v):
        raise TypeError("'ImmutableDict' objects are immutable")

    def __delitem__(self, v):
        raise TypeError("'ImmutableDict' objects are immutable")

    def setdefault(self, k, default=...):
        raise TypeError("'ImmutableDict' objects are immutable")
