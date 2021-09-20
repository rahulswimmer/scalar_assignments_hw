def solve(A,B):
    outputArr=[]
    K=2
    if K>len(A): K=K%len(A)

    start=0
    end=len(A)-1
    while start < end:
        temp=A[start]
        A[start]=A[end]
        A[end]=temp
        start+=1
        end-=1

    start=0
    end=K-1
    while start < end:
        temp=A[start]
        A[start]=A[end]
        A[end]=temp
        start+=1
        end-=1

    start=K
    end=len(A)-1
    while start < end:
        temp=A[start]
        A[start]=A[end]
        A[end]=temp
        start+=1
        end-=1
    print(A)
    

    print(A)
A=[1,2,3,4,5]
B=[2,3]
solve(A,B)