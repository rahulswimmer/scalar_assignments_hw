def solve():

    A = [2, 4, 8, 10, 6, 13]
    minDifference = A[1]-A[0]
    count = 0

    A.sort(reverse=True)

    for i in range(1, len(A)-1):
        if A[i+1]-A[i] < minDifference:
            minDifference = A[i+1]-A[i]
            count = 1
        elif A[i+1]-A[i] == minDifference:
            count += 1

    print(count)


solve()
