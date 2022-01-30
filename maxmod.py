import sys

def solve(A):
    A.sort()

    i = 0
    j = len(A)-1
    ans = -sys.maxsize-1

    while i <= j:
        if A[i] % A[j] > ans:
            ans =  A[i] % A[j]
        i += 1
    
    return ans

A=[2,6,4]
print(solve(A))