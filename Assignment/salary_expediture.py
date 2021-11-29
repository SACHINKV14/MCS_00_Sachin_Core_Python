""""create user with name eid total salary(basics,house rent allowance ,special allowance ,tax deduction)(inputs)




"""

def salary_input(num_of_months):
    for i in range(0,len(salary)):
        salary_value=int(input("enter the salary given for "+ '\t'+ salary[i] + ":"))
        salary_amount.append(salary_value)
         # salary_per_month[salary] = salary_amount
    net_salary=sum(salary_amount[0:len(salary)-1]) - salary_amount[3]
    print("net_salary is:", net_salary)
    saving_for_all_months = num_of_months * net_salary
    return saving_for_all_months


def enter_expend(n_expden):
   for i in range(0, n_expden):
      expenses = input("Enter expences names : ")
      amount_expenses = int(input("Enter amount spend for expences : "))
      expences[expenses] = amount_expenses
   exp_amount=sum(expences.values())
   return exp_amount

salary_amount=[]
expences={}
name=input("Enter the employer name:")
eid=input("Enter the employer id:")
num_of_months=int(input("Enter the number of months:"))
salary=('house_allowance','basic','special_allownace','tax')
n_expden=int(input("number of expenditure:"))
total_income = salary_input(num_of_months)
total_expenditure = enter_expend(n_expden)

if total_income < total_expenditure:
    print("your a loser")
else:
   print("your winner")





