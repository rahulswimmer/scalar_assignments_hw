def trap(A):
    l = []
    l.append(A[0])
    r = []
    r.append(A[len(A)-1])
    sum=0
    

    for i in range(1,len(A)):
        l.append(max(A[i],l[i-1]))
   
    for i in range(len(A)-2,-1,-1):
        r.append(max(A[i],r[len(A)-2-i]))
    r.reverse()

    for i in range(1,len(A)-1):
        sum += min(l[i],r[i])-A[i]
    

A=[0,1,0,4,1,0,1,3,1,1,2]
print(trap(A))