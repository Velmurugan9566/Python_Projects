def divideArray(nums, k):
    
    l=len(nums)
    print(nums)
    nums.sort()
    if l%3 != 0:
        return []
    index=0
    print(nums)
    ans=[]
        
    for i in range(l//3):
        t=[]
        for j in range(3):
            t.append(nums[index])
            index +=1
        ans.append(t)
        print(ans)
        if ans[i][2] - ans[i][0] >k :
            return []
    return ans


nums = [1,3,4,8,7,9,3,5,1]
k = 2
divideArray(nums,k)

    
