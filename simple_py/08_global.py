num = 0
def func(n):
    if n == 0:
        # print(num)
        # local variable 'num' referenced before assignment
        global num
        print(num)
    else:
        num = num + n
        func(n-1)
func(10)