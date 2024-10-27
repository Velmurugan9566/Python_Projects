'''#using While Loop
rows = int(input("Enter number of rows: "))
i = 1
while i <= rows:
    space = 1
    while space <= (rows - i):
        print(end="  ")
        space += 1
    k = 0
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    print()
    i += 1

row = int(input('Enter number of rows: '))
i = row
while i > 0:
    j = row - i
    while j > 0:
        print(' ', end='')  
        j -= 1
    j = 2 * i - 1
    while j > 0:
        print('*', end='') 
        j -= 1
    print()
    i -= 1
   ''' 
#Using For loop
row = int(input('Enter number of rows: '))
for i in range(row,0,-1):
    for j in range(row-i):
        print('', end=' ')
    for j in range(2*i-1):
        print(i,end=' ')
    print()
'''
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print('1',end="  ")

    for k in range(2 * i - 1):
        print("* ", end=" ")

    print()'''

