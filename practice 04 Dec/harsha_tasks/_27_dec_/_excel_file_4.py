#writing items in rows and columns in excel sheet
header=['id','name','phone number']
ids=[1,2,3,4]
names=['sachin','virat','dravid','dhoni']
phnum=[113,114,115,116]

import xlsxwriter
wb=xlsxwriter.Workbook('cric_playeers.xlsx')
ws=wb.add_worksheet(name='deatils')

#for headers
r0 = 0
c0 = 0
for i1 in header:
    ws.write(r0,c0,i1)
    c0+=1

r1=1
c1=0
for id in ids:
    ws.write(r1,c1,id)
    r1+=1
r2=1
c2=1
for name in names:
    ws.write(r2,c2,name)
    r2+=1

r3=1
c3=2
for pnum in phnum:
    ws.write(r3,c3,pnum)
    r3+=1

wb.close()