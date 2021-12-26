def sort(A,B):
    ansArr=[]

    i=0
    j=0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            ansArr.append(A[i])
            i+=1
        else:
            ansArr.append(B[j])
            j+=1

    if i < len(A):
        ansArr += A[i:]
    if j < len(B):
        ansArr += B[j:]
    
    return ansArr

A=[2,3,4,10]
B=[9,15,19]
print(sort(A,B))