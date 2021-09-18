def solve(A,B):
    outpurArr=[]
    for i in B:
        outpurArr.append(shiftByK(A,i))
    return outpurArr       

def leftRotateOnebyOne(A):
    temp=A[0]

    for i in range(len(A)-1):
        A[i]=A[i+1]
    A[len(A)-1]=temp
    return A

def shiftByK(A,B):
    K=B
    temp=A.copy()
    for i in range(K):
        leftRotateOnebyOne(temp)
    return temp

A=[17, 100, 11, 5]
B=[1]
print(solve(A,B))
#print(shiftByK(A))