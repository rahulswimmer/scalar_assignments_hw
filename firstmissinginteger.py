def solve(A):
    vst = [0 for x in range(len(A))]
    flag=len(A)+1
    
    ## code for tc o(n) and sc o(n)
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= len(A):
                vst[A[i]-1]=1

    if len(A)==1 and A[0]>0:
        return A[0]+1
    elif len(A)==1 and A[0]<0:
        return 1
 
    for i in range(len(vst)):
        if vst[i]==0:
            flag=i+1
            break

    return flag
    

A=[1,2,3,4,5,6]
print(solve(A))