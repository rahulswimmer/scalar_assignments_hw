def solve(A,B):
    hashmap={}
    ans=0
    outputArr=[]

    for i in range(B):
        if A[i] in hashmap:
            hashmap[A[i]]+=1
        else:
            hashmap[A[i]]=1
        if hashmap[A[i]]==1:
            ans+=1
    
    outputArr.append(ans)

    for i in range(B,len(A)):
        if A[i] in hashmap:
            hashmap[A[i]]+=1
        else:
            hashmap[A[i]]=1
        if hashmap[A[i]]==1:
            ans+=1

        hashmap[A[i-B]]-=1
        
        if hashmap[A[i-B]]==0:
            ans-=1
        outputArr.append(ans)

    return outputArr

A=[1,2,1,3,4,3]
B=3
print(solve(A,B))