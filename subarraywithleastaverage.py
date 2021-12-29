import sys

def solve(A,B):
    ans = sys.maxsize 

    sumA = sum(A[0:B])
    ans = min(ans,sumA)
    ind = 0

    for i in range(B,len(A)):
        sumA += A[i]
        sumA -= A[i-B]
        if ans > sumA:
            ans = sumA
            ind = i-B+1

    return ind
    



A=[3, 7, 90, 20, 10, 50, 40]
B=3
print(solve(A,B))