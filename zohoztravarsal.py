# Python3 program to print 
# square matrix in Z form 
def diag(arr, n):
    for i in range(n):
        for j in range(1,n):
            if(i == 0):
               print(arr[i][j], end = " ") 
    	    elif(j == n-(i+1)):
               print('\n')
               print(arr[i][j], end = " ")
	       print('\n')
    	    elif(i == n - 1): 
	    	print(arr[i][j], end = " ") 

# Driver code 
if __name__ == '__main__': 
	a= [ [ 4, 5, 6, 8 ], 
		[ 1, 2, 3, 1 ], 
		[ 7, 8, 9, 4 ], 
		[ 1, 8, 7, 5 ] ] 

	diag(a, 4) 
# This code is contributed by mohit kumar 29 and improved by Hari Aditya
