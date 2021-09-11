def solve():
    A = [1, 2, 3, 4]
    B = 8
    goodPairCount = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if i != j and (A[i]+A[j] == B):
                goodPairCount += 1
    return goodPairCount


print(solve())
