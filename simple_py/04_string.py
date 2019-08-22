# python 2 与 python 3 在 Unicode 字符串上存在不同
str1 = "Hello World"
print(str1[1:4])  # ell
print("123" == "123")  # True
print(str1[:6] + "Bob!")  # Hello Bob!
print("o" in str1)  # True

print(str1.find("o"))  # 4
print(str1.rfind("o"))  # 7
print(str1.replace("o", "z"))  # Hellz Wzrld
print(str1.join("123"))  # 1Hello World2Hello World3
print(str1.split("o"))  # ['Hell', ' W', 'rld']
print(str1.split("o", 1))  # ['Hell', ' World']
print(str1.upper())  # HELLO WORLD

# 转义字符      描述
# \(在行尾时)   续行符
# \\	       反斜杠符号
# \'           单引号
# \"           双引号
# \a           响铃
# \b           退格(Backspace)
# \e           转义
# \000         空
# \n           换行
# \v           纵向制表符
# \t           横向制表符
# \r           回车
# \f           换页
# \oyy         八进制数，yy代表的字符，例如：\o12代表换行
# \xyy         十六进制数，yy代表的字符，例如：\x0a代表换行
# \other       其它的字符以普通格式输出
