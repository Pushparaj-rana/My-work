import time
import threading

def square(arr):
    print('sqare of given num')
    for i in arr:
        time.sleep(0.5)
        print(f'square is : {i*i}')

def cube(arr):
    print('cube of given num')
    for i in arr:
        time.sleep(0.5)
        print('cube', i*i*i)

arr=[1,2,3,4,5]

t = time.time()
# square(arr)
# cube(arr)

t1 = threading.Thread(target=square,args=(arr,))
t2 = threading.Thread(target=cube,args=(arr,))

t1.start()
t2.start()

# t1.join()
# t2.join()

print('time taken:', time.time()-t)


'''EXCERCISE'''

# import time
# import threading
# from threading import Thread

# def sleepMe(i):
#     print(f"Thread {i} will sleep.")
#     time.sleep(1)
#     print("Thread %i is awake" % i)


# t =  time.time()

# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()
#     th.join()
#     print("Current Threads: %i." % threading.active_count())
# print('time taken:', time.time()-t)


