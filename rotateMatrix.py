def solve(A):
    N = len(A)
 
    for i in range(N):
        for j in range(i):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
 
    for i in range(N):
        for j in range(N//2):
            temp = A[i][j]
            A[i][j] = A[i][N-j-1]
            A[i][N-j-1] = temp
    return A


A=[[1,2],[3,4]]
print(solve(A))