"""finding the percentage of 6 subjects"""

subject=[10,20,30,40,50,60]
m,s,so,k,h,e=subject


# input_score= input('Enter a six score value: ').spilt()
#
# subject=input_score.split()
# m,s,so,k,h,e=input_score.split()
'''type casting'''

print("score in maths: ", m)
print("score in science: ", s)
print("score in social: ", so)
print("score in kannada: ", k)
print("score in hindi: ", h)
print("score in english: ", e)
print()


total = m + s + so + k + h + e
print('total is :',total)
# score1 = [90, 91, 92, 93, 94, 95]
count = 0
average = total / 6.0
percentage = (total / 600.0) * 100
count=0
if average == 100:
    print("Student awarded gold medal")
elif 90 in subject:
    print("s its there")
    for i in subject:
         if i > 89 and i < 95:
            count = count + 1
            if count >2 and count<7:

                    print('he scored above 90 in three subjects')
elif average > 90 and average < 95:
    print("Student got distinction")
elif average > 75 and average < 90:
    print("Student got first class")

