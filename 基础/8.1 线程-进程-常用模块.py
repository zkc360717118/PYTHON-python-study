#第一部分： 多线程 Tread模块

import threading
import time

def my_counter():
    i = 0
    for _ in range(100):
        i = i+1
        print(threading.current_thread().name)
    return True

#顺序执行单个线程
def shunxun():
    start_time = time.time()
    for tid in range(2):
        t = threading.Thread(target=my_counter)
        t.start()
        t.join()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))



# if __name__ == '__main__':
#     shunxun()

#同时执行 2个并发线程
def bingxing():
    thread_array = {} #字典
    start_time = time.time()
    for tid in range(2):
        t = threading.Thread(target=my_counter)
        t.start()
        t.join()
        thread_array[tid] = t

    for i in range(2):
        thread_array[i].join()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

# if __name__ == '__main__':
#     bingxing()


#第二部分 多线程fork操作
# import os
# print("process (%s) START..." % os.getpid())
#
# pid = os.fork()
# if pid==0:
#     print(" i  am child process(%s) and my parent is ($s)"% (os.getpid(),os.getppid()))
# else:
#     print(" i  am parent process(%s) and my sone is ($s)"% (os.getppid(),os.getpid()))
#


#第三部分 multiprocessing 多线程模块
from multiprocessing import Process
import time

def f(n):
    time.sleep(1)
    print( n*n)

# if __name__ == "__main__":
#     for i in range(10):
#         p = Process(target=f, args=[i,])
#         p.start()


#第四部分： 多进程之间的通信Queue
from multiprocessing import Process,Queue
import time

def write(q):
    for i in ["A","B","C","D","E"]:
        print( 'PUT %s TO quere' % i)
        q.put(i)
        time.sleep(0.5)

def read(q):
    while True:
        v = q.get(True)
        time.sleep(0.5)
        print('get %s from queue' %v)

# if __name__ == "__main__":
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     pw.start()
#     pw.join()
#     pr.start()
#     pr.join()
#     pr.terminate()

#第五部分 进程池
from multiprocessing import Pool
import  time

def f(x):
    print(x*x)
    time.sleep(2)
    return x*x

if __name__ == "__main__":
    #定义启动的进程数量
    pool = Pool(processes=5)
    res_list = []

    #循环10次执行上面的方法，由于使用了进程池，并且有5个进程先把前面5个计算出来了，然后空闲的进程再去计算剩下的
    for i in range(10):
        res = pool.apply_async(f,[i,]) # 异步
        print('---------:',i)
        res_list.append(res)

    pool.close()
    pool.join() # 保证了上面线程池执行完了，然后代码往下执行

    for r in res_list:
        print("result",r.get(timeout=5))






