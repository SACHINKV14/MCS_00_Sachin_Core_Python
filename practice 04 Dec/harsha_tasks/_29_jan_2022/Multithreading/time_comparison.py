#comparisons between codes with and without usingthrAFD
import time

def d2(n):
    for x in n:
        print(x%2)

def d3(n):
    for x in n:
        print(x%3)

n=[2,4,3,6,7]
s=time.time()
d2(n)
d3(n)
e=time.time()
print(e-s)   #diff between end and start time
print("-------------------------------")
import threading
def d2(n):
    for x in n:
        print(x%2)

def d3(n):
    for x in n:
        print(x%3)

n=[2,4,3,6,7]
s=time.time_ns()
t1=threading.Thread(target=d2,args=(n,))
t2=threading.Thread(target=d3,args=(n,))

t1.start()
t2.start()

t1.join()
t2.join()

e=time.time_ns()
print("e",e)
print("s",s)
print("e-s",e-s)