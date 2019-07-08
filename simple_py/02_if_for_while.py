print("if/else ...")
a = 1
if a == 1:
    print("a = 1")
elif a == 2:
    pass
else:
    pass

b = None
if not b:
    print("not b")

if "a" in "abcd":
    print("a in abcd")

if a == 1 and "a" in "abcd":
    print("a == 1 and a in abcd")

print("\nfor ......")
for i in [1, 2, 3, 4]:
    print(i)

print("\nwhile ....")
num = 3
while num > 0:
    print(num)
    num -= 1

# 注意冒号和缩进，空格和TAB不能混用

print("\nbreak/continue ...")
for i in range(10):
    if i == 4:
        break
    else:
        print(i)
        continue

