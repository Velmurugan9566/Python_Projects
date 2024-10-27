a=[1,2,3,4]
def generate_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            subarrays.append(subarray)
    su=0
    for i in range(len(subarrays)):
        su=su + min(subarrays[i])
    print(su)

    return su

arr = [11,81,94,43,3]
result = generate_subarrays(arr)

print("Input array:", arr)
print("Subarrays are:", result)

