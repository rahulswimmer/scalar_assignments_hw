def mergeSort(A,l,r):
    count=0
    if l < r:
        m = (r+l)//2
        count += mergeSort(A, l, m)
        count += mergeSort(A, m+1, r)
        count += merge(A, l, m, r)
    return count%1000000007

def merge(A,l,m,r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = A[l + i]

    for j in range(0, n2):
        R[j] = A[m + 1 + j]

    i = 0
    j = 0
    k = l
    count = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            count+=(n1-i)
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
    return count

class Solution:
    def solve(self, A):
        ans = mergeSort(A,0,len(A)-1)
        return ans