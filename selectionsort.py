def sort(A):
    index=0
    for i in range(len(A)):
        index=i
        for j in range(i+1,len(A)):
            if A[index] > A[j]:
                index=j
        A[i],A[index] = A[index],A[i]
    return A

A=[5,3,2,6,7,8,1]
print(sort(A))