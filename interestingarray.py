def solve(A):
    xorans = 0

    for i in A:
        xorans ^= i

    if xorans % 2 == 0:
        return "Yes"
    else:
        return "No"

A=[9,17,9,17,24,7879]
print(solve(A))