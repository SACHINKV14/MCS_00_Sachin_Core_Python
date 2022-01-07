import pandas as pd

#read data from excel
df = pd.read_excel("gfg.xlsx", sheet_name="Sheet1")
print(df)
print("---------------")
#write data into excel
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
# df1.to_excel("output.xlsx")
#To specify the sheet name:
df1.to_excel("output.xlsx",
             sheet_name='Sheet_name_1')

#to write into multiple pagews in excel

df2 = df1.copy()
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')

#ExcelWriter can also be used to append to an existing Excel file:
with pd.ExcelWriter('output.xlsx',mode='a') as writer:
    df.to_excel(writer, sheet_name='Sheet_name_3')