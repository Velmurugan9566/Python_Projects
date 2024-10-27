#program for exception handler routines
#zero division error
try:
    num1=int(input('Enter the Numerater: '))
    num2=int(input('Enter the denaminater: '))
    div=num1//num2
    print('Division of two numbers :',div)
except ZeroDivisionError:
    print('!!..Zero division is not passible..')
except:
    print('!!...Some error has occured..')


#file access error
try:
    fname=input('Enter the file name:')
    f=open(fname,'r')
    print(f.read())
except IOError:
    print('!!...File not found')


#list index out of range
try:
    li=[]
    n=int(input('Enter the no of element:'))
    for i in range(n):
        e=int(input('Enter the Elements: '))
        li.append(e)
    print(li)
    ch=int(input('Enter the index number you want view the element: '))
    print('Index no:{}:{}'.format(ch,li[ch]))
except IndexError:
    print('oops..!!! List index out of range..')
except:
    print('!..some error has occoured..')
    
