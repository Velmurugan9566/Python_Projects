#program to calculate EB bill data from csv file using csv modules
from tabulate import tabulate
import csv
import pandas as pd
def units(s,e): #function for calculate eb charge
    unit=int(e)-int(s)
    if unit<=50:
        cost=unit*30
    elif unit<=100:
        cost=50*30+(unit-50)*35
    elif unit<=150:
        cost=(50*30)+(50*35)+(unit-100)*40
    else:
        cost=(50*30)+(50*35)+(50*40)+(unit-150)*50
    return cost
with open('eb.csv', mode='r') as f:#open csv file
    csfile=csv.reader(f)#read csv file using reader fucntion
    head=['Customer Id','Customer Name','Total Cost']
    da=[]
    next(csfile)
    for li in csfile:#accessing line by line in csv file
        tu=units(li[2],li[3])#call the function for calculation 
        da.append([li[0],li[1],tu])    
    print(tabulate(da,headers=head,tablefmt='grid'))

#csf=pd.read_csv('eb.csv')
#print(csf)

'''f=open('eb.csv','r')
print(f)
for i in f:
    s=i.split(',')
    print(s)'''
