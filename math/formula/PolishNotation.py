import random


# 逆波兰表达式：a+d*(b-c)--->a,d,b,c,-,*,+
def reverse_polish_notation(infix):
    temp_list = []
    suffix = []
    for op in infix:
        if op == ')':
            while True:
                a = temp_list.pop()
                if a == '(':
                    break
                suffix.append(a)
        elif op == '(':
            temp_list.append(op)
            pass
        elif op in '+-*/':
            while temp_list:
                # 栈内的操作符优先级高的时候直接输出
                def op1_bigger(op1,op2):
                    if op1 in "*/":
                        return True
                    if op1 in "+-":
                        if op2 in "+-":
                            return True
                    return False

                if op1_bigger(temp_list[-1],op):
                    a = temp_list.pop()
                    suffix.append(a)
                else:
                    break
            temp_list.append(op)
            pass
        else:
            suffix.append(op)
    while temp_list:
        a = temp_list.pop()
        suffix.append(a)
    return suffix


def calc_rpn(suffix):
    list1 = []
    for op in suffix:
        if op in "+-*/":
            val1 = list1.pop()
            val2 = list1.pop()
            str_temp = str(val2)+op+str(val1)
            val3 = eval(str_temp)
            list1.append(val3)
        else:
            list1.append(op)
    assert(len(list1) == 1)
    return list1[0]


a = random.random()
b = random.random()
c = random.random()
d = random.random()
e = random.random()
f = random.random()

# test
infix1 = "a+b*(c-d)"
print(eval(infix1))
suffix1 = reverse_polish_notation(infix1)
print(suffix1)
print(calc_rpn(suffix1))
assert(eval(infix1) == calc_rpn(suffix1))

infix1 = "a+b*(c-d)*e"
print(eval(infix1))
suffix1 = reverse_polish_notation(infix1)
print(suffix1)
print(calc_rpn(suffix1))
assert(eval(infix1) == calc_rpn(suffix1))

infix1 = "a-((a-b-f)*c-d)*e"
print(eval(infix1))
suffix1 = reverse_polish_notation(infix1)
print(suffix1)
print(calc_rpn(suffix1))
assert(eval(infix1) == calc_rpn(suffix1))
