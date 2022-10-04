'''# Data Driven Testing
# Suppose we have some test cases which need a test data And
# we have to execute same test case multiple times with different test data this known as a data driven testing.
# We prepare the data in Excel or Database, but we use Excel to prepare the data.
# Selenium webdriver doesn't support Excel sheet,
# By openpyxl module we can work with Excel files(.xlsx) '''


# How to Read data from Excel

'''import openpyxl
path="D:\Selenium\Calling Data.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook["Call History"]
Rows=sheet.max_row
Columns=sheet.max_column
print("No of Rows",Rows)
print("No of Columns",Columns)
for r in range(1,Rows+1):
  for c in range(1,Columns+1):
      print(sheet.cell(r,c).value,end='         ')
      print()'''

# How to Write data in to Excel

'''import openpyxl
path="D:\Selenium\Calling Data.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook["xyz"]
Rows=sheet.max_row
Columns=sheet.max_column
print("No of Rows",Rows)
print("No of Columns",Columns)
for r in range(1,Rows+1):
  for c in range(1,Columns+1):
      print(sheet.cell(r,c).value,end='         ')
      print()'''


# THIS FILE NOT COMPLETED