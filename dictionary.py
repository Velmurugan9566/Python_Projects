n=int(input('enter the no of student: '))
stu={}
for i in range(n+1):
    li=input().split()
    name=li[0]
    marks=list(map(float,li[1:]))
    stu[name]=marks
choice=list(stu)[-1]
print(stu)
a=stu.popitem()
print(a)
ave=sum(stu[choice])/len(stu[choice])
print("{:.2f}".format(ave))

