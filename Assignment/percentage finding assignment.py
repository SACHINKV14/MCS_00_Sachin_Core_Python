n_subs = []
num = int(input('number of  subjects: '))
for n in range(num):
    numbers = int(input('Enter subject marks '))
    n_subs.append(numbers)
    total=sum(n_subs)
print("total marks scored is :", total)
average = total / num
percentage = (total / (num*100)) * 100


if percentage == 100:
    print("Student awarded gold medal")
elif 90 in n_subs:
    print("s its there")
    for i in n_subs:
         if i > 89 and i < 95:
            count = count + 1
            if count >2 and count<7:
                pass
            print('he scored above 90 in three subjects')
elif average > 90 and average < 95:
    print("Student got distinction")
elif average > 75 and average < 90:
    print("Student got first class")
else:
    print("student is failed")