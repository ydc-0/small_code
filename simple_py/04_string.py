# python 2 与 python 3 在 Unicode 字符串上存在不同, 这儿都是使用 python3
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
print(str1.count('o')) # How many 'o' in str1

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


# input 获取一行输入，split 可以将输入按空格切割转换为数组
s = input("input:").split()  # <- 123 456
print(s)
print(int(s[0])+int(s[1]))
# python2 中 raw_input 输入字串， input 输入表达式
a = 1
print("a=%s"%a)
print("a="+str(a))
print("a={}".format(a))
print(", ".join(["1", "2", "3"]))
# format 格式化 https://www.runoob.com/python/att-string-format.html


s = b"123\xe5456"
# print(s.decode('utf-8'))
#'utf-8' codec can't decode byte 0xe5 in position 3: invalid continuation byte
print(s.decode("utf8","ignore")) # 123456
print("abcde".encode('utf-8')) # b'abcde'
