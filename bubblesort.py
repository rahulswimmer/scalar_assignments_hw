def sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

A=[5,3,2,6,7,8,1]
print(sort(A))