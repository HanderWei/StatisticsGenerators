from openpyxl import load_workbook

wb = load_workbook(filename='statistics.xlsx')
ws = wb['Android']

i = 0

for row in ws.rows:
    if row[7].value is not None:
        print(row[7].value)
    # if len(row) > 6:
    #     for cell in row:
    #         i = i + 1
    #         args = (i, cell.value)
    #         print("%d: %s" % args)
