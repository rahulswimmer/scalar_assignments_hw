def mergeSort(A):
    if len(A) > 1:
        m = len(A)//2
        L = A[:m]
        M = A[m:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            A[k] = M[j]
            j += 1
            k += 1
    return A



A=[3,2,9,4,10]
print(mergeSort(A))