import xlwt, xlrd




# Initialize a workbook
# book = xlwt.Workbook(encoding="utf-8")
#
# # Add a sheet to the workbook
# sheet1 = book.add_sheet("Python Sheet 1")
# sheet2 = book.add_sheet("Python Sheet 2")
# sheet3 = book.add_sheet("Python Sheet 3")
#
# # Write to the sheet of the workbook
# ## CASE 1
# sheet1.write(0, 0, "This is the First Cell of the First Sheet")
# ## CASE 2
# data = ['Jack', 'Dwite', 23, '12.12.1992', 90400]
# for num, i in enumerate(data):
#     sheet2.write(0, num, i)
# ## CASE 3
# for i in range(25):
#     for j in range(10):
#         sheet3.write(i, j, j)
#
# # Save the workbook
# book.save("spreadsheet.xls")

### read
read_data = xlrd.open_workbook('spreadsheet.xls')
r_sheet1 = read_data.sheet_by_index(0)
r_sheet2 = read_data.sheet_by_index(1)
r_sheet3 = read_data.sheet_by_index(2)

row_1 = r_sheet1.row_values(0)
print(row_1)

row_2 = r_sheet2.row_values(0)
print(row_2)

for rownum in range(r_sheet3.nrows):
    row_data = r_sheet3.row_values(rownum)
    print(row_data)
