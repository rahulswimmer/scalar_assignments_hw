def solve(A,B):
    if A == 1 or B == 1:
        return 0
    x = solve( A - 1, B//2)

    if B%2 == 1:
        return x
    return 1-x

A=2
B=2
print(solve(A,B))