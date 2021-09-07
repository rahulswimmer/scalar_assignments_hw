def solve():
    A = [0]
    A.sort(reverse=True)

    for i in range(0, len(A)):
        if (A[i] == i and A[i] != A[i-1]) or A[0] == 0:
            return 1
    return -1


print(solve())
