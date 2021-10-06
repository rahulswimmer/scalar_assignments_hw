def solve(A):
    sumArr = sum(A)
    ans = 0
    A.sort()
    for i in range(len(A)-1, -1, -1):
        ans += sumArr
        sumArr -= A[i]
    return ans


A = [8, 0, 10]
print(solve(A))
