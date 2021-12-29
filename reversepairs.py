def solve(A):
    A.sort()
    count = 0

    i = 0
    j = len(A)-1

    while i < len(A) and j < len(A):
        if A[i] > 2*A[j]:
            count +=1
        i += 1
        j -= 1

    return count

A=[1,1,2,3,3]
print(solve(A))