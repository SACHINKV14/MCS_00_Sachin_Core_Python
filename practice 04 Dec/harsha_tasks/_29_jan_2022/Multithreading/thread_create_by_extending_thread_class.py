#by extending thread class

#can only override run and innit method
from threading import *
import threading

#in class threading.Thread should be used
class A(threading.Thread):
    def run(self):
        for x in range(7):
            print("Child..",current_thread().getName())

obj=A()
obj.start()
obj.join()
print("control returned to ",current_thread().getName())