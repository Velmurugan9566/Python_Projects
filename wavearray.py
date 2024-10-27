a=[1,2,3,4,5,6,7,8]
j,k=0,1
while (k<=len(a)):
    a[j],a[k]=a[k],a[j]
    j += 2
    k += 2
print(a)
    
from matplotlib import matplot

