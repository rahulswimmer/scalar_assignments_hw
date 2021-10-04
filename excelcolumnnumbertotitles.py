import math
def solve(A):
    res=''
    while A > 0:
        if A%26 == 0:
            res = 'Z' + res
            A = math.floor(A/26 -1)
        else:
            res = chr(ord('A') + A%26 - 1) + res
            A = math.floor(A/26)
    return res

A=980089
print(solve(A))
