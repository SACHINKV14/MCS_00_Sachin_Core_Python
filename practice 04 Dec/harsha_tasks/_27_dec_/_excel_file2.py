#writing names in row wise by for loops
#for writing it always start in row =0 cloumn =0
import xlsxwriter

wk=xlsxwriter.Workbook('mcs1.xlsx')

ws=wk.add_worksheet(name='details')

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0
names=['sachin','dravid','virat','dhoni']
for item in names:
    ws.write(row,column,item)
    row+=1
    # column+=1
wk.close()