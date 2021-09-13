def solve(A):
    maxVal = max(A)
    val = 0

    for i in A:
        val += (maxVal-i)
    return val


A = [1, 1, 1, 1]
solve(A)
