n = int(input())
s=set()
for i in range(n):
    si=int(input())
    s.add(si)
num_commands = int(input('no of comma:'))

for _ in range(num_commands):
    command = input('command').split()
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        element = int(command[1])
        s.remove(element)
    elif command[0] == 'discard':
        element = int(command[1])
        s.discard(element)

print(sum(s))
