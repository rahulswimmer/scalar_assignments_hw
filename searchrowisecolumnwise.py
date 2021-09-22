def solve(A,B):
    sum=0
    # for i in range(len(A)):
    #     for j in range(len(A[0])):
    #         if A[i][j]==B:
    #             return (i+1)*1009+(j+1)
    # return -1
    i=0
    j=len(A[0])-1
    
    while i<len(A) and j>=0:
        if A[i][j]==B:
            return (i+1)*1009+(j+1)
        elif A[i][j] > B:
            j-=1
        else:
            i+=1
    return -1

A=[[2, 8, 8, 8],
  [2, 8, 8, 8],
  [2, 8, 8, 8]]
B=8
print(solve(A,B))