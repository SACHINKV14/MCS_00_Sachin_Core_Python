
#without creating a class

from threading import *
def new():
    for x in range(6):
        print("child Executing...",current_thread().getName())

t1=Thread(target=new)
print(current_thread().getName())
t1.start()    #allwos to execute first thread
t1.join()   #to make sure child thread to finish first we use this without this bye will print after executiung first thtread once


print("Bye",current_thread().getName())  #executes main thread