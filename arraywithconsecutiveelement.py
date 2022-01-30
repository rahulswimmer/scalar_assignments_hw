def solve(A):
    B = A.copy()
    A.sort()

    for i in range(len(A)):
        if abs(A[i]-A[i+1]) != 1:
            print(A[i]-A[i+1])
            return 0
    return 1


A=[3,2,1,4,6]
print(solve(A))