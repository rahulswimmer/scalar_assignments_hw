def solve(A):
    if str(A)==str(A)[::-1]:
        return True
    else:
        return False

A='000'
print(solve(A))