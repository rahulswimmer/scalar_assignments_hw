def solve(A):
    temp = A.copy()
    A.sort()
    ans=[]
    idx1=0
    idx2=0

    l=0
    r=len(A)-1

    if A == temp:
        return ans.append(-1)
        return ans
    
    while l <= r:
        if A[l] != temp[l] and len(ans)==0:
            idx1=l
            break
        l+=1

    while r >= l:
        if A[r] != temp[r]:
            idx2=r
            break
        r-=1
    ans.append(l)
    ans.append(r)
    return ans

A=[1,2,3,7,8,4,9,10]
print(solve(A))