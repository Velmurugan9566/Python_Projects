import os
files=os.listdir()
print('avilable files')
for i in files:
    print(i)
fn=input('Enter the file you want to open/Create')
if os.path.exists(fn):
    print('file already exists')
f=open(fn,'w')
try:
    print('Start writting\nTo stop writting press ctrl+c')
    while True:  
        con=input()
except:
    f.write(con)
    print('content are written successfully')
    f.close()

#Read file content   
print('Read the content in: ',fn)
o=open(fn,'r')
print(o.read())
ch=input('Do you want to count file characters (1/0): ')
if ch==1:
    fcount=open(fn,'r')
    fstr=fcount.read()
    li=1
    w=0
    c=0
    s=0
    wc=0
    t=''
    for i in fstr:
        if t !=' ' and (i==' ' or i=='\n'):
            w +=1
        if i=='\n':
            li +=1
        if i !=' ' and  i !='\n':
            c +=1
        wc +=1
        t=i
    print('word: ',w,'line: ',li,'character: ',c,'With space character: ',wc)
else:
    exit()
fcount.close()
'''c=fcount.readlines()
print(c.count(' '))
c=fcount.read()
print(type(c))'''

