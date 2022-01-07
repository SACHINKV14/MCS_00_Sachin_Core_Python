# writing items in rows and columns in excel sheet
header = ['id', 'name', 'phone number']
ids = [1, 2, 3, 4]
names = ['sachin', 'virat', 'dravid', 'dhoni']
phnum = [113, 114, 115, 116]
import xlsxwriter
wb = xlsxwriter.Workbook('students.xlsx')
ws = wb.add_worksheet(name='deatils')
# for headers
r0 = 0
c0 = 0
for i1 in header:
    ws.write(r0, c0, i1)
    c0 += 1
#using loops
c1=0
for r1,id,name,pnum in zip(range(1,5),ids,names,phnum):
    ws.write(r1, c1, id)
    ws.write(r1, c1+1, name)
    ws.write(r1,c1+2,pnum)

wb.close()