def solve(A):
    prefixSumArr = []
    hashmap={}
    ans=0

    hashmap[0]=-1

    for i in range(len(A)):
        if A[i]==0:
            A[i]=-1

    prefixSumArr.append(A[0])

    for i in range(1,len(A)):
        prefixSumArr.append(A[i]+prefixSumArr[i-1])

    for i in range(len(A)):
        if prefixSumArr[i] in hashmap:
            ans = max(ans,i-hashmap[prefixSumArr[i]])
        else:
            hashmap[prefixSumArr[i]]=i

    return ans


A=[1, 0, 1, 0, 1,1,0,0,1]
print(solve(A))