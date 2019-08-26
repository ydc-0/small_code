import copy

print("list ...")
list1 = ['aa', 'bb', 'cc']
print(len(list1))
for item in list1:
    print(item)

list1 = [1, 2, 3]
print(list1)

list1 = list("hello,world")
print(list1)

list1 = [i for i in range(10)]
print(list1)

list1 = [["a", "b"], ["c", "c"]]
print(list1, len(list1))
print(list1[0])

list1 = [1, 2]
list2 = [2, 3]
print("add : ", list1 + list2)
print("set : ", set(list1 + list2))
print("set : ", list(set(list1 + list2)))

print("\ndict ....")
dict1 = {"a": 1, "b": 2}
print("keys: ", dict1.keys())
for key in dict1.keys():
    print(key, dict1[key])

# copy / deep copy
print("\ncopy/deepcopy ...")
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict1["a"] = 3
print(id(dict1),id(dict2))
print(dict1, dict2)

dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()
dict1["a"] = 3
print(dict1, dict2)

dict1 = {"a": [1, 2], "b": 2}
dict2 = dict1.copy()
dict1["a"][1] = 21
dict1["b"] = 33
print(dict1, dict2)

dict1 = {"a": [1, 2], "b": 2}
dict2 = copy.deepcopy(dict1)
dict1["a"][1] = 21
print(dict1, dict2)

import random

list1 = [1,2,3,4,5,6,7]
random.shuffle(list1)
print(list1)
list2 = list1[0:3]
print(list2)

print("-----generate list-----")
list1 = [True] * 2 + [False] * 3
print(list1)
list1 = [1, "a"] * 5
print(list1)
list1 = [random.randint(1,5)] * 5  # same number
print(list1)
import numpy
list1 = numpy.random.randint(10, size=5)
print(list1)