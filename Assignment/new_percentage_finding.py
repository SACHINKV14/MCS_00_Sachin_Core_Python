def enter_sub_marks(num):                              #function
   for n in range(0,num):                              #for a range
     subjects = input('Enter subject name:')           #getting keys
     numbers = int(input('Enter subject marks: '))     #getting values
     sub_marks[subjects] = numbers           #creating dictionary
   print(sub_marks)
   print(type(subjects))

def renter_sub_marks():
    for key, value in sub_marks.items():
        if (value < 75):
            print("Enter marks of subject ", key, " : ")
            sub_temp = int(input())
            sub_marks[key] = sub_temp

def grade():
    total=0
    for i in sub_marks.values
    total +=i
    percentage = (total / (num * 100)) * 100

num = int(input('number of  subjects: '))
sub_marks={}
enter_sub_marks(num)
count=0
if num>=3 and num<=7 :
        grade()
        if percentage>90:
            print("Distinction")
        elif percentage>=75 and percentage<=90:
            print("Average")
        elif percentage<75:
            for i in n_marks:
                if  i < 75:
                   count += 1
                   if count <= 3:
                       print("Chance again")
                       reenter_sub_marks()
                       grade()
                   else :
                       print("fail")