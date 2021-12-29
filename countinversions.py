def solve(A):
    count=0
    if len(A) > 1:
        m = len(A)//2
        L = A[:m]
        M = A[m:]

        solve(L)
        solve(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = M[j]
                j += 1
                count+=m-i+1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            A[k] = M[j]
            j += 1
            k += 1
    return count



A=[3,2,9,4,10]
print(solve(A))