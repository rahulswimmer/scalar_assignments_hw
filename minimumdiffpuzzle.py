import sys

def solve(A,B):
    A.sort()
    ans=sys.maxsize

    for i in range(len(A)-B+1):
        if A[i+B-1]-A[i] < ans:
            ans = A[i+B-1]-A[i]

    return ans

A=[10, 12, 10, 7, 5, 22]
B=4
print(solve(A,B))