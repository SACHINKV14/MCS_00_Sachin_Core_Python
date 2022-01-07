#reading from one excel file writing it into
#other excel files based on the groups

import pandas as pd

# read DataFrame
data = pd.read_excel("Customers.xlsx")

#We will filter the columns based on the specific column name Gender to its values
male = data[data['Gender'] == 'Male']
female = data[data['Gender'] == 'Female']

male.to_excel('Gender_male.xlsx')
female.to_excel('Gender_female.xlsx')

# print(pd.read_csv("Gender_male.csv"))
# print(pd.read_csv("Gender_female.csv"))