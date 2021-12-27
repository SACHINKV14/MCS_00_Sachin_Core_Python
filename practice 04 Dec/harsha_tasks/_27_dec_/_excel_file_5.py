# writing items in rows and columns in excel sheet
header = ['id', 'name', 'phone number']
ids = [1, 2, 3, 4]
names = ['sachin', 'virat', 'dravid', 'dhoni']
phnum = [113, 114, 115, 116]

import xlsxwriter

wb = xlsxwriter.Workbook('cric_player.xlsx')
ws = wb.add_worksheet(name='deatils')

# for headers
r0 = 0
c0 = 0
for i1 in header:
    ws.write(r0, c0, i1)
    c0 += 1
#using loops
c1 = 0
for r1,id in zip(range(1,5),ids):
    ws.write(r1, c1, id)
c2 = 1
for r1,name in zip(range(1,5),names):
    ws.write(r1,c2,name)
c3=2
for r1,pnum in zip(range(1,5),phnum):
    ws.write(r1,c3,pnum)

wb.close()