# '''
# We have to take input of subjects and marks from user
# If No.of subjects is between 3 - 7
# 	We have to find percentage of all subjects
# 	If total percentage is greater than 90 --> awarded distinction
# 	If total percentage is between 75 to 90 --> awarded average
# 	If total percentage is less than 75:
# 		chance is given only if he score less than 75% in 3 subjects
# 		if he score less than 75% in more than 3 subjects he is given fail
#
#
# If No.of subjects is greater than 7
# 	we have to find percentage of all subjects
# 	If total percentage is greater than 90 --> awarded distinction
# 	If total percentage is between 75 to 90 --> awarded average
# 	If total percentage is less than 75:
# 		chance is given only if the fail subjects average should be between 65 - 75
# 		else he will be given fail
# 		if he fail in more than 5 subjects he should be debard
# ''''''

n_subs = []
n_marks=[]
num = int(input('number of  subjects: '))
for n in range(num):
    subjects = input('Enter subject name:')
    numbers = int(input('Enter subject marks: '))
    n_subs.append(numbers)
    n_marks.append(subjects)

# dictionary = dict(zip(n_subs, n_marks))
dictionary = dict(zip(n_subs,n_marks))
print(dictionary)

if num>2 and num<8:
        total = sum(n_marks)
        percentage = (total / (num * 100)) * 100
        if percentage>90:
            print("Distinction")
        elif percentage>74 and percentage<91:
            print("Average")
        elif percentage<76:
            for i in n_marks:
                if  i < 75:
                   count = count + 1
                   if count < 4:
                      print("fail")
                   else :
                       for n in range(num + 1):
                           subjects = input('Enter subject name:')
                           numbers = int(input('Enter subject marks: '))
                           n_subs.append(numbers)
                           n_marks.append(subjects)
                       total = sum(n_marks)
                       percentage = (total / (num * 100)) * 100
                       if percentage<76:
                           print("fail")

if num>7:
  if percentage > 90:
        print("Distinction")
  elif percentage > 74 and percentage < 91:
        print("Average")
  elif percentage < 76:
        countfail=0
        for i in n_marks:
            if i < 75:
                countfail=countfail+1
                for i in range(n_marks):
                    totalfail=sum()
                    average_fsubs=totalfail / countfail
                    if avearage_fsubs < 76 and avearage_fsubs>64:
                        print("chance is given")
                    else:
                        print("fail")
