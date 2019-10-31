import queue
import threading
import time


work_q = queue.Queue(10)
q_lock = threading.Lock()


class Factory(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
        self.stop_event = threading.Event()

    def run(self):
        while True:
            is_stop = self.stop_event.wait(timeout=self.delay)
            if is_stop:
                print("{}: {} stop".format(time.ctime(time.time()), self.name))
                break
            with q_lock:
                work_q.put("from {}".format(self.name))

    def stop(self):
        self.stop_event.set()


factory_list = []
for i in range(1, 4, 1):
    fac = Factory("factory{}".format(i), i)
    fac.start()
    factory_list.append(fac)

for _ in range(13):
    product = work_q.get(block=True)
    print("{}: {}".format(time.ctime(time.time()), product))

for fac in factory_list:
    fac.stop()

while True:
    time.sleep(1)
    for fac in factory_list:
        if fac.is_alive():
            continue
    else:
        break
