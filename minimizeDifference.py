import sys

def solve(A,B):
    mins=-sys.maxsize-1
    A.sort()

    for _ in range(B):
        A[len(A)-1]-=1
        A[0]+=1
        mins = max(A[len(A)-1])-min(A[0])
    return mins

A = [2, 6, 3, 9, 8]
B=3
print(solve(A,B))