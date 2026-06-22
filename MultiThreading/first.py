import threading
import time
def f1():
    print("Hello")
    time.sleep(2)
    print("Hi")
def f2():
    print("welcome")
    time.sleep(2)
    print("Bye Bye")
t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Main thread ends")