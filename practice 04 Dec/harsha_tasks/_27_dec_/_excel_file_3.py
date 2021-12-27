#writing names in row wise by for loops

import xlsxwriter

wk=xlsxwriter.Workbook('mcs2.xlsx')

ws=wk.add_worksheet(name='details')

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0
names=['id','name','phone number','mail id']
for item in names:
    ws.write(row,column,item)
    column+=1
wk.close()