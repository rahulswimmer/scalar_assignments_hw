def solve(A, B):
    i = 0
    j = len(A)-1
    count = 0

    while i < j:
        if A[i]+A[j] == B:
            count += 1
            i += 1
            j -= 1
        elif A[i]+A[j] > B:
            j -= 1
        elif A[i]+A[j] < B:
            i += 1
    
    return count

A=[1,2,3,4,5]
B=5
print(solve(A,B))