import xlrd
import os
stu='Book1.xls'
b=xlrd.open_workbook(stu)
she=b.sheet_by_index(0)
row=she.nrows
col=she.ncols
print(row)
print(col)
for i in range(row):
    print("\n-------------------------\n")
    for j in range(col):
         print(she.cell_value(i,j),end="\t")
    print("||")
print("\n-------------------------\n")

'''
import pandas as pd
d=pd.read_excel('Book1.xls')
print(d)
'''
         
