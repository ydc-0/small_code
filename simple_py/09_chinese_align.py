# 中文字符串的对齐
# 汉字的unicode编码 ： https://www.qqxiuzi.cn/zh/hanzi-unicode-bianma.php


# 使用 len 获取到的字符串长度中，一个中文字符仅记一
# 我们可以用下面几种方法获取中文的个数
def chinese_num1(s):
    # 在 'utf-8' 编码下 一个中文的长度为 3
    # 如果这儿使用 'gb2312' 编码 每个中文的长度就是 2
    return (len(s.encode('utf-8')) - len(s)) // 2


def chinese_num2(s):
    # 利用 ord 或 unicode 编码值
    # 正则中也常用 [\u4e00-\u9fa5] 匹配中文 [^\x00-\xff] 匹配双字节字符
    # 注意这儿的 unicode 不包括中文标点
    # return sum([1 if '\u4e00' <= ch <= '\u9fff' else 0 for ch in s])
    return sum([1 if ord(ch) > 127 else 0 for ch in s])


strr = "一二三四五六七八九十"
print(len(strr), len(strr.encode('utf-8')))  # 10 30
print("{:>30s}".format("test"))
print(" " * (30 - chinese_num1(strr) - len(strr)) + strr)
print(" " * (30 - chinese_num2(strr) - len(strr)) + strr)


c = [
    '一',
    '一二',
    '一二三',
    '一二三四',
    '一二三四五',
    '一二三四五六',
    '一二三四五六七'
]
print('------格式化1 (format，未对齐)：-------')
for s in c:
    print('|%20s|' % s)
print('------格式化2 (rjust，未对齐)：-------')
for s in c:
    # 字符串提供 ljust center rjust 方法，也可自定义填充字符
    # 效果与 format 一致
    print('|' + s.rjust(20) + '|')
print('------格式化3 (计算中文个数)：-------')
for s in c:
    fill_len = 20 - len(s) - chinese_num1(s)
    print("|" + " " * fill_len + s + "|")
print('------格式化4 (填充中文空格)：-------')
for s in c:
    # chr(12888) 为中文空格， 这种方法只能解决纯中文
    print('|{0:{1}>10}|'.format(s, chr(12288)))


# format 方法格式补充：
# |  :  | <填充字符> | <对齐方式> | <宽度> | ,(千位分隔符) | <.精度> |  <类型>  |
# | 引导 | 补全用字符 | <^> 左中右 | 总len |  输出数字专用  | 小数用 | sdfex%... |
