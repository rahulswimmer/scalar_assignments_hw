def solve(A):
    if A == 0:
        return 0
    return A%10+solve(A//10)


A=46
print(solve(A))