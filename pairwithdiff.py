def solve( A, B):
    i = 0
    j = 1
    count = 0
    A.sort()
    n= len(A)
    while j < len(A)-1:
        if A[j]-A[i] == B:
            count += 1
            x,y= A[i],A[j]
            while(i < n and A[i] == x):
                i += 1
            while(j < n and A[j] == y):
                j += 1
        elif A[j]-A[i] > B:
            i += 1
            if i == j:
                j += 1
        elif A[j]-A[i] < B:
            j += 1
            
    return count

A= [ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ]
B=3
print(solve(A,B))