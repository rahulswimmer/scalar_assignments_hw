def solve(A):
    if str(A)==str(A)[::-1]:
        return True
    else:
        return False

A='101'
print(solve(A))