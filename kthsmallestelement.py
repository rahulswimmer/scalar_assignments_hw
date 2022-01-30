def solve(A, B):
    for i in range(B):
        k = i
        for j in range(i+1, len(A)):
            if A[k] > A[j]:
                k = j
        A[i], A[k] = A[k], A[i]
    print(A[B-1])


A = (8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66,
     35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92)
B = 9
solve(A, B)
