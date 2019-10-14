# input() / print()
# python2 中有 input() 和 raw_input(), 区别是 input() 读表达式
# python3 中只有 input() 读字符串
# input() 可以带参数打印提示信息
# input() 遇到回车结束
st1 = input()
st2 = input("please input：")
print("1:{},2:{}".format(st1,st2))

# sys.stdin sys.stdout
# read readline readlines
# sys.stdin.read() 与 input 的区别是 read 直到输入 ctrl+D 才结束
# NOTE: 在 windows 中调试没能成功, 在 linux 上 ctrl+D 可用
import sys
st1 = sys.stdin.read()
print("read:{}".format(st1))
