import serial
import time
import threading


class SerialRecv(threading.Thread):
    def __init__(self, ser):
        self.ser = ser
        self._running = threading.Event()
        super().__init__()

    def run(self):
        self._running.set()
        while self._running.isSet():
            data = self.ser.read(1000)
            if not data:
                continue
            # print(data)
            print(str(data, 'UTF-8'))

    def stop(self):
        self._running.clear()


try:
    ser = serial.Serial('COM41', 115200, timeout=0.01)
except Exception as e:
    print(e)
    exit(0)
ser_recv = SerialRecv(ser)
ser_recv.start()
while True:
    instr = input()
    if instr == "exit":
        ser_recv.stop()
        exit(0)
    ser.write(bytes(instr+'\r\n', encoding='utf-8'))