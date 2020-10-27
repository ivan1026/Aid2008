'''

'''

from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working")


# 位置字传参
# p = Process(target=worker, args=(2, "levi"))

# 关键字传参
p = Process(target=worker, kwargs={"name": "Tom", "sec": 2})
p.start()
p.join()

print("======================")
