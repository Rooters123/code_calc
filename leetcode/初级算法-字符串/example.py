# encoding = utf-8
from threading import Thread,Lock,RLock
import time
# 互斥锁
# node_lock = Lock()
# fork_lock =  Lock()

node_lock = fork_lock = RLock()
def eat1(name):
    # 吃面前的准备
    node_lock.acquire()
    print("%s拿到面"%name)

    fork_lock.acquire()
    print("%s拿到叉子"%name)

    print("%s开始吃面"%name)

    # 吃面后的准备
    fork_lock.release()
    node_lock.release()

def eat2(name):
    # 吃面前的准备,这里是先拿叉子，
    fork_lock.acquire()
    print("%s拿到叉子" % name)

    node_lock.acquire()
    print("%s拿到面"%name)
    # 这里可以保证一定会产生死锁现象
    time.sleep(1)

    print("%s开始吃面"%name)

    # 吃面后的准备
    node_lock.release()
    fork_lock.release()

# Thread(target=eat1,args=("zbr",)).start()
# Thread(target=eat2,args=("wdq",)).start()
# Thread(target=eat1,args=("ljy",)).start()
# Thread(target=eat2,args=("lw",)).start()


class test():
    def __init__(self):
        self.name = "zbr"
    @classmethod
    def classFunc(cls):
        print("我是类方法")
        pass
    @staticmethod
    def staticFunc():
        print("我是静态方法")

        pass

a = test()
a.classFunc()
