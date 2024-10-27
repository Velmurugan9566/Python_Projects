#1.list
'''print(str(88.7).ljust(10,' '))
n=int(input("Enter the no of students:"))
name=[]
mark=[]
for i in range(n):
    na=input("Enter the name:")
    name.append(na)
    t=[]
    for j in range(5):
        m=int(input("Enter the marks:"))
        t.append(m)
    mark.append(t)
    per=[]
for i in mark:
    ave=sum(i)/len(i)
    per.append(ave)
c=0
for i in per:
    if i>=90 and i<=100:
        print(name[c].ljust(20,' '),str(per[c]).ljust(5,' '),': Excellent Performance')
    elif i<=89 and i>=70:
        print(name[c].ljust(20,' '),str(per[c]).ljust(5,' '),': Very Good Performance')
    elif i<=69 and i>=50:
        print(name[c].ljust(20,' '),str(per[c]).ljust(5,' '),': Good Performance')
    elif i<=49:
        print(name[c].ljust(20,' '),str(per[c]).ljust(5,' '),': Super Performance')
    c+=1


#2.Tuple
print(type(int('ab')))


from tabulate import tabulate
n=int(input('Enter the no of Students:'))
name=()
int_m=()
sem=()
assign=()
mark=()
total=0
td=[]
for i in range(n):
    li=[]
    na=input('Enter the Name:')
    name=(*name,na)#unpacking
    for j in range(3):
        li.append(int(input('Enter marks(max 15):')))
    li=sorted(li,reverse=True)
    int_m=(*int_m,li)
    sem=(*sem,(int(input('Enter Seminar mark(max 5):'))))
    assign=(*assign,(int(input('Enter Assignment mark(max 5):'))))
for k in range(n):
    intmark=sum(int_m[k][0:2])/2
    total=intmark+sem[i]+assign[i]
    print(total)
    mark=(*mark,total)
td.append([name,int_m,sem,assign,mark])
head=['stuname','Intmark','seminar','assignment','total']
table=tabulate(td,head,tablefmt='grid')
print("-----------------------------------------\n")
print("S.No  Student Name\t Total")
for i in range(n):
    print(i+1,".\t",name[i],"\t\t",mark[i])
print("----------------------------------------- \n")

#3.Dictionary

n=int(input('Enter the no of students:'))
stuname=[]
stumark=[]
for i in range(n):
    name=input('Enter the Student name: ')
    stuname.append(name)
    t=[]
    for j in range(5):
        marks=int(input('Enter the subject mark(max 100): '))
        t.append(marks)
    stumark.append(t)
#print(stuname)
#print(stumark)
print('\n')
dic={}
c=0
for i in stumark:
    ave=sum(i)/len(i)
    dic[stuname[c]]=ave
    c+=1
#print(dic)
sortdic=sorted(dic.items(), key=lambda x:x[1],reverse=True)
#print(type(sortdic))
print('\t\tTop 3 Ranked Students are:\n')
for i in range(len(sortdic)):
    name,mark=sortdic[i]
    print(i+1,'.',name,"\t:",mark)
    if i+1==3:
        break


#4.set

n=input('Enter the Number: ')
c=n.split()
char=list(set(c))
result=[]
for i in char:
    cou=0
    li=[]
    li.append(i)
    for j in c:
        if i==j:
            cou+=1
    li.append(cou)
    result.append(li)
max2=[]
result.sort(key=lambda x:x[1],reverse=True)
for i in range(1,len(result)):
    if result[0][1]==result[i][1]:
        max2.append(result[i])
for j in range(len(result)-2,0,-1):
    if result[len(result)-1][1]==result[j][1]:
        print('small two')
print('Result in list:',result)
if max2:
    print('There is more the same occurence of digits:')
print("Highest Occurence of digit is: ",result[0][0]," in ",result[0][1],"times")
print("Least Occurence of digit is: ",result[len(result)-1][0]," in ",result[len(result)-1][1],"time")


li=[2,44,1,57,33,89,-1,99]
le=len(li)
for i in range(le):
    s=i
    print(s,'s')
    for j in range(i+1,le):
        print(j)
        if li[s]>li[j]:
            s=j
    li[i],li[s]=li[s],li[i]
            
print(li)
'''

#8.Classes and functions
import sys
class xyz_bank:
    def __init__(self,c_name,acc_no,balance,acc_type):
        self.customer_name=c_name
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
    def credit(self,amount):
        if amount>0:
            self.balance+=amount
            print('Money Credited.')
            print('Available Balance:',self.balance)
        else:
            print('Invalid amount')
    def debit(self,amount):
        if amount>0 and amount<=(self.balance-100):
            self.balance-=amount 
            print('Money Debited.')
            print('Available Balance:',self.balance)
        else:
            print('Insufficient Balance')
    def open_termdeposit(self,principle,year):
        if self.acc_type=='Sr.Citizen':
            interest=0.12
        else:
            interest=0.10
        si=principle*year*interest
        total_amount=principle+si
        print('\tOpen Term Deposit Amount: ',total_amount)
    def display(self):
        print('\t\t',self.customer_name,'\'s Details')
        print('Customer Name: ',self.customer_name,'\nAccount Number:',self.acc_no,'\nAccount Type:',self.acc_type,'\nAvailable Balance: ',self.balance)
print('\t\tWelcome to Xyz Bank\n \t\t Please Enter your Details\n')       
n=input('Enter your Name:')
ac=input('Enter your Account Number:')
ba=int(input('Enter the Balance Amount:'))
while True:
    t=int(input('Enter the type of account (1.General,2.Sr_Citizen):'))
    if t == 1:
        ty='General'
        break
    elif t == 2:
        ty='Sr_citizen'
        break
    elif t == 3:
        ty='Minor'
        break
    else:
        print('Choice the correct number ....next time :')
print(ty)
c2=xyz_bank(n,ac,ba,ty)
while True:
    ch=int(input('Enter Your choice.\n1.Credit Amount\n2.Debit Amount\n3.Open_term_Deposit.\n4.Display Details\n5.Exit\n'))
    if ch==1:
        am=int(input('Enter the Amount you want to Credit:'))
        c2.credit(am)
    elif ch==2:
        am=int(input('Enter the Amount you want to Debit:'))
        c2.debit(am)
    elif ch==3:
        am=int(input('Enter the Amount you want to find open_term_deposit:'))
        y=int(input('Enter the year:'))
        c2.open_termdeposit(am,y)
    elif ch==4:
        c2.display()
    elif ch==5:
        break
    else:
        print('Please Enter valid choice')
