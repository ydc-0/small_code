import _thread
import threading
import time

# python3 中 thread 模块已被废弃，推荐使用 threading
# python3 thread 菜鸟教程
# https://www.runoob.com/python3/python3-multithreading.html


class MyThread(threading.Thread):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count

    def run(self):
        print("开始线程：" + self.name)
        while self.count:
            with L_lock:
                L.append(self.count)
                self.count -= 1
                print("线程{}：L：{}".format(self.name, L))
            time.sleep(1)
        print("退出线程：" + self.name)


L = []
L_lock = threading.Lock()
thread1 = MyThread("a", 4)
thread2 = MyThread("b", 3)

# 守护进程&线程 ： https://blog.csdn.net/u013210620/article/details/78710532
# Java 版： https://blog.csdn.net/weiwosuoai/article/details/89387280
# setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
# 这个的意思是，把B设置为守护线程，
# 需要在 start 之前调用
thread1.setDaemon(True)

thread1.start()
thread2.start()
# join 方法将一直等待线程退出
thread1.join()
thread2.join()


# thread提供了低级别的、原始的线程以及一个简单的锁。
def print_time(name, count):
    while count:
        count -= 1
        print("thread {}: {}".format(name, time.ctime(time.time())))
        time.sleep(1)


try:
    _thread.start_new_thread(print_time, ("1", 3))
    _thread.start_new_thread(print_time, ("2", 4))
except:
    print("Error: 无法启动线程")


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exit")
        exit(0)
