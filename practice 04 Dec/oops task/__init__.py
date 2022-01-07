# 75 Write a Python program to convert month name to a number of days
month75=[['jan',31],['feb',28],['mar',31],['apr',30]]
mon75=input("to know num of days in a month,\nenter first three letters of the month: ").lower()
days75=[]
for x75 in month75:
    if mon75==x75[0]:
        days75.append(month75[0][1])
print(f'number of days month \"{mon75}\" contains is :{days75[0]} ')
