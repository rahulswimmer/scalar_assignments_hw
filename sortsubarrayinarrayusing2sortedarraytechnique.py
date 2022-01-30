def solve(A):
    l = 2
    y = 5
    r = 7

    L = A[l:y]
    R = A[y:r+1]

    print(L,R)

A=[8,1,3,6,11,2,4,9,7,6]
print(solve(A))