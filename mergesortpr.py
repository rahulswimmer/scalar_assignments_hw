def mergeSort(A,l,r):
    if l < r:
        m = l + (r - l)//2 
        print(m)
        L = A[:m]
        R = A[m:]
        print(L,R)
        mergeSort(A,l,m)
        mergeSort(A,m+1,r)
    

A=[3,2,9,4,10]
n=len(A)
l=0
r=len(A)-1
print(mergeSort(A,l,r))