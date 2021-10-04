def solve(A,B):
    outputArr=[]
    for i in B:
        outputArr.append(rotate(A,i))
    return outputArr
    
def rotate(A,K):
    R=[]
    if K>len(A): K=K%len(A)
    for i in range(K, len(A)):
        R.append(A[i])
    for i in range(K):
        R.append(A[i])
    return R
    
A= [ 6, 31, 33, 13, 82, 66, 9, 12, 69, 21, 17, 2, 50, 69, 90, 71, 31, 1, 13, 70, 94, 46, 89, 13, 55, 54, 67, 97, 28, 27, 62, 34, 41, 18, 15, 35, 13, 84, 93, 27, 89, 23, 6, 56, 94, 40, 54, 95, 47 ]
B=[ 88, 85, 98, 36, 66, 40, 30, 26, 51, 77, 62, 60, 92, 64, 53, 86, 24, 53, 85, 49, 57, 29, 32, 60, 75, 82, 17, 23, 67, 51, 23, 11, 70, 59 ]
print(solve(A,B))