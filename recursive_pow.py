def solve(A,n,C):
    if A == 0:
        return 0
    if n == 0:
        return 1
    x = solve(A,n>>1,C)
    if A % 2 == 0:
        return (x * x)%C
    else:
        return (A * x * x)%C

A=-1
n=2
C=20
print(solve(A,n,C))