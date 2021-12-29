import sys

def solve(A):
    minDiff = sys.maxsize
    A.sort()
    for i in range(len(A)-1):
        minDiff = min(minDiff,abs(A[i]-A[i+1]))
    return minDiff

A=[5,17,100,11]
print(solve(A))