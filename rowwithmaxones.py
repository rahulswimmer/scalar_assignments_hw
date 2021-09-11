def solve(A):
    maxSum=0
    maxIndex=0
    for i in range(len(A)):
        sum=0
        for j in range(len(A[i])):
            sum += A[i][j]
        if maxSum < sum:
            maxSum=sum
            maxIndex=i
    return maxIndex
    
    

   
A=[[1,0,0,1],[1,1,0,1]]
print(solve(A))