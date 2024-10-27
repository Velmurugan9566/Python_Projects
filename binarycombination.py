n=2
arr=[]
i=n<<1
print(i)
for i in range(i<<n):
    arr.append(i ^ (i>>1))
print(arr)
