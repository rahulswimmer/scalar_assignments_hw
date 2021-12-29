import math

def solve(A):
    bit = int(math.log(A, 2)) + 1
    x = 0

    for i in range(0, bit):
        if A & (1 << i):
            continue
        else:
            x += 1 << i

    y = 1 << bit
    ans = x ^ y
    return ans

A=9
print(solve(A))
