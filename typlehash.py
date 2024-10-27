n = int(input("Enter the number of elements: "))
integer_list = map(int, input("Enter space-separated integers: ").split())

t = tuple(integer_list)
result_hash = hash(t)

print(result_hash)
