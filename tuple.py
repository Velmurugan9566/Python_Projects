n=int(input('enter no of stu'))
name=()
int_m=()
sem=()
assign=()
mark=()
total=0

for i in range(n):
    li=[]
    na=input('enter the name:')
    name=(*name,na)#unpacking
    for j in range(3):
        li.append(int(input('enter mark:')))
    li=sorted(li,reverse=True)
    int_m=(*int_m,li)
    sem=(*sem,(int(input('enter seminar mark:'))))
    assign=(*assign,(int(input('enter Assignment mark:'))))
for k in range(n):
    intmark=sum(int_m[k][0:2])/2
    total=intmark+sem[i]+assign[i]
    print(total)
    mark=(*mark,total)
    
print("S.No  Student Name\tIntenel mark(best two)\tSeminar mark\tAssignment Mark\t Total")
for i in range(n):
    print(i,".",name[i],"\t",int_m[i][0:2],"\t\t",sem[i],"\t\t",assign[i],"\t\t",mark[i])
print(int_m)
print(name)
print(sem)
print(assign)
print(mark)

    
