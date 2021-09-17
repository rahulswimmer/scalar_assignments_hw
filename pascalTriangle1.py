def solve(A,N):
    for i in range(1,N):
        col=[]
        col.append(1)
        for j in range(len(A[i])-1):
            col.append(A[i][j]+A[i][j+1])
        col.append(1)
        A.append(col)
    return A
A=[[1],[1,1]]
N=4
print(solve(A,N))