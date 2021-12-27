#reading from one excel file writing it into
#writing into mutiple sheets

import pandas as pd

# read DataFrame
data = pd.read_excel("Customers.xlsx")

#We will filter the columns based on the specific column name Gender to its values
male = data[data['Gender'] == 'Male']
female = data[data['Gender'] == 'Female']


with pd.ExcelWriter('Customers1.xlsx') as writer:  # doctest: +SKIP
    data.to_excel(writer,sheet_name='Details')
    male.to_excel(writer, sheet_name='Sheet_name_1')
    female.to_excel(writer, sheet_name='Sheet_name_2')