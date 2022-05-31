#!/usr/bin/python3
import socket
import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 10086))

        msg = "lalalala demaxiya"
        s.send(msg.encode("utf-8"))
        print(self.name, " recv: ", s.recv(1024).decode())
        time.sleep(self.delay)
        s.close()
        print(self.name, " is over")

# 创建新线程
thread1 = myThread("Thread-1", 2)
thread2 = myThread("Thread-2", 5)

# 开启新线程
thread1.start()
thread2.start()

# 等待所有线程完成
thread1.join()
thread2.join()

print ("退出主线程")