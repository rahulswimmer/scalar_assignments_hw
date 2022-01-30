def wave(A):
    A.sort()
    for i in range(len(A)-1):
        if i % 2 == 0:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
    return A

A=[2,1]
print(wave(A))