def solve(A,B):
    hashmap={}
    ans=0

    for i in range(B):
        if A[i] in hashmap:
            hashmap[A[i]]+=1
        else:
            hashmap[A[i]]=1
        if hashmap[A[i]]==1:
            ans+=1
    
    # for i in range(B,len(A)-1):
    #     hashmap[A[i]]+=1
    #     hashmap[A[i-B]]-=1
        
    #     if hashmap[A[i]]==1:
    #         ans+=1
    #     if hashmap[A[i-B]]==0:
    #         ans-=1

    return ans

A=[3,7,5,5,4,6,1]
B=4
print(solve(A,B))