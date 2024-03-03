import openpyxl

path = "/Users/deepintent/Downloads/Test1.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1, 5):
    for c in range(1, 6):
        sheet.cell(r, c).value = "Welcome"

workbook.save(path)
