# import time
#
#
# def calc_square(numbers):
#     print("calculate square of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print('sqaure:',n*n)
#
# def calc_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print('cube:',n*n*n)
#
# arr = [2,3,8,9]
#
# t = time.time()
# calc_square(arr)
# calc_cube(arr)
# print("program took ",time.time()-t)


print("-------------------------------------------------------")
import time
import threading

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.10)
        print('sqaure:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.10)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()     #runs two functions parallelly
t2.start()

t1.join()
t2.join()     #join  waits unntil the square func runs


print("program took ",time.time()-t)

