
#program 1
def naturalnum_asc(n):
    if n <= 0:
        return
    else:
        naturalnum_asc(n-1)
        print(n)
def naturalnum_des(n):
    if n <= 0:
        return
    else:
        print(n)
        naturalnum_des(n-1)


n=int(input('Enter the Number :'))
print('First ',n,'Natural number in Ascending order')
naturalnum_asc(n)
print('First ',n,'Natural number in Descending order')
naturalnum_des(n)

#program 2
def fact(n):
    if n<=0:
        return 1
    else:
        return n * fact(n-1)
        

n=int(input('Enter the number : '))
ans=fact(n)
print('Factorial of ',n,' is: ',ans)

#program 3
def sum_naturalnum(n):
    if n > 0:
        print(n)
        return n + sum_naturalnum(n-1)
    else:
        return 0

n=int(input('Enter the number :'))
s=sum_naturalnum(n)
print('Sum of first ',n,'number is :',s)


#program 4
def cal_power(b,e):
    if e<=0:
        return 1
    else:
        return b * cal_power(b,e-1)

n=int(input('Enter the base number :'))
e=int(input('Enter the power digit :'))
ans=cal_power(n,e)
print(ans)

    
