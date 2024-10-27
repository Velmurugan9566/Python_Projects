'''from array import *
new=array('i',[])
s=array('i',[3,45,53,2,23,9])
for i in s:
    print (i)
le=len(s)
for i in range(0,le):
    print(i)
    if (s[i]%2==0)or(s[i]%3==0):
        new.append(s[i])
print(new)
leap=array('i',[])
nleap=array('i',[])
#n=int(input('Enter the Year'))
for n in range(1900,2023):
    if(n%100==0)and(n%400==0):
        leap.append(n)
    elif(n%4==0)and(n%100!=0):
        leap.append(n)
    else:
        nleap.append(n)
print(leap)
print(nleap)

num=int(input('enter the number'))

rev=''
hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while(num!=0):
    tem=num%16
    rev=hexa[tem]+rev
    num=num//16
print(rev)'''

n=[2,66,23,98,66,76,87]
max=n[0]
for i in range(7):
    for j in range(i+1,7):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]        
print(n)
print(vel.upper())
