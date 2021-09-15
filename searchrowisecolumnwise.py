def solve(A,B):
    sum=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==B:
                return (i+1)*1009+(j+1)
    return -1

A=[[1,2,3],[4,5,5],[7,8,9]]
B=5
print(solve(A,B))