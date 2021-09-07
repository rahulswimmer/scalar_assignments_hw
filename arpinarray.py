def solve():
    A = [3, 5, 2]
    A.sort(reverse=True)
    diff = A[1]-A[0]

    if len(A) == 1:
        return 1

    for i in range(1, len(A)-1):
        if diff != A[i+1]-A[i]:
            return 0
    return 1


print(solve())
