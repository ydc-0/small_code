import os
import subprocess
import ctypes
import sys

# 如何获得管理员权限
# https://blog.csdn.net/qq_17550379/article/details/79006655
# https://blog.csdn.net/qq_17550379/article/details/79006718
# print(ctypes.windll.shell32.IsUserAnAdmin())

# 1. 使用 os.system 可以直接调用系统命令
# 返回值表示程序执行是否成功
os.system('echo hello world')
ret = os.system('aaaa')
print(ret)

# 2. os.popen 可以获取命令的输出
py_ver = os.popen('python -V').read()
print(py_ver)

# 3. subprocess 用来运行其他程序的库
# 参考资料：https://www.cnblogs.com/zhoug2020/p/5079407.html
# 3.1 call 类似于 os.system 更多参数和调用方式
subprocess.call(['dir', '.'], shell=True, cwd='C:/proj')
subprocess.call('echo -----------------------------', shell=True)

# 3.2 Popen 可以用于交互
#     os.popen 也使用了 subpress
#     实时输出 https://blog.csdn.net/u012206617/article/details/84560895
cmd = subprocess.Popen('cmd.exe', shell=True,
                       stdin=subprocess.PIPE, stdout=subprocess.PIPE)
cmd.stdin.write(b'ping www.baidu.com\r\n')
cmd.stdin.write(b'exit\r\n')  # 如果不退出后边会卡在 stdout.read
cmd.stdin.flush()
# 使用 poll 检查子进程有没有关闭
while cmd.poll() is None:
    line = cmd.stdout.readline()
    # Popen 有 encodeing 参数还没试
    print(line.decode('gbk'), end='')

#  3.2 check_call 执行并检查返回值，失败抛出异常
try:
    subprocess.check_call('abcdef',shell=True)
except subprocess.CalledProcessError as e:
    print(e)
    print(e.returncode)