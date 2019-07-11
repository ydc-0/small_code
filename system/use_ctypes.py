from ctypes import *

# load the shared object file
adder = cdll.LoadLibrary('./_static/func64.so')
# windows 下无法调用 so 文件
# 32 位和 64 位无法同时工作

# Find sum of integers
sum_int = adder.add_int(4, 5)
print('Type: ', type(sum_int))
print('Sum of 4,5 is: ', str(sum_int))


# Find sum of floats
a = c_float(2.3)
b = c_float(4.5)
add_float = adder.add_float
add_float.restype = c_float

print('Sum of 2.3 and 4.5 is: ', add_float(a,b))


# Use C Structure
class ST(Structure):
    _fields_ = [
            ("a", c_int),
            ("b", c_char * 30),
            ("p", c_void_p)
            ]

    def __repr__(self):
        return "{a:%s, b:%s, p:%s}" % (self.a, self.b, self.p)


get_struct = adder.get_struct_res
get_struct.restype = ST
print("Get C structure: ", get_struct())

