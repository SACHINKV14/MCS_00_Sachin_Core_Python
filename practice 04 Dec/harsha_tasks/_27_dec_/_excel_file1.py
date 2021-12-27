#



# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet(name='details')
# sheet2=workbook.add_worksheet(name='sheet2')
# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'id')
worksheet.write('B1', 'name')
worksheet.write('C1', 'phone number')
worksheet.write('D1', 'mail')

# sheet2.write('d5',369)
# Finally, close the Excel file
# via the close() method.
workbook.close()