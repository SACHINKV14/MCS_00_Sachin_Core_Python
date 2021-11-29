'''enter name of month ask for salary : hra , basic , special , tax
"Do you want to enter another month" y/n
if yes continue
if no
enter expenses:
cost of expense:
"Do you have any other expenses ?" (y/n)
if yes continue
else
"DO you want to enter expense for another month?"'''

def salary_input(salary):
    total_salary=0
    for i in range(0,len(salary)):
        salary_value=float(input("enter the salary given for "+ '\t'+ salary[i] + ":"))
        salary_amount.append(salary_value)
    monthly_salary=sum(salary_amount[0:len(salary)-1]) - salary_amount[3]
    return monthly_salary

salary_amount=[]
name=input("Enter the employer name:")
eid=input("Enter the employer id:")
salary=('house_allowance','basic','special_allownace','tax')
total_salary=salary_input(salary)

total_expenditure=0
total_months=0
flag1=1
while(flag1):
        if(flag1 != -1):
            print("--------------------")
            month = input("Enter month name : ")
            print("--------------------")
            total_months += 1
            flag2 = 1
            while(flag2):
                if(flag2 != -1):
                    print("--------------------")
                    exp_name = input("Enter expenditure name : ")
                    exp_cost = int(input("Enter expenditure cost : "))
                    print("--------------------")
                    total_expenditure += exp_cost
                another_expenditure = input("Do you want to enter another expenditure (y/n) : ")
                if(another_expenditure == "y"):
                    flag2 = 1
                elif(another_expenditure == "n"):
                    flag2 = 0
                else:
                    print("WRONT INPUT. ENTER EXPENDITURE AGAIN : ")
                    flag2 = -1
        another_month = input("Do you want to enter another month (y/n) : ")
        if (another_month == "y"):
            flag1 = 1
        elif (another_month == "n"):
            flag1 = 0
        else:
            print("WRONG INPUT. ENTER MONTH AGAIN : ")
            flag1 = -1
print(total_months, total_expenditure)


savings = (total_salary * total_months) - total_expenditure
print("----------------------------------------")
print("Monthly Salary getting  :",total_salary)
print("---------------------------------------------")
print("total expences for",total_months,"months is :",total_expenditure)
print("-------------------------------------------------------")
print("total savings have from your",total_months,"months of salary is :",savings)