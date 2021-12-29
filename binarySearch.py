def solve(A,k):
    l=0
    r=len(A)-1
    m=0
    while l<=r:
        m=l+(r-l)//2 
        if k == A[m]:
            return m

        if k < A[m]:
            r=m-1
        else:
            l=m+1
    return -1

A=[1,3,5,7,9,10,11,13,15,17,30,35,40]
print(solve(A,117))