from copy import deepcopy

def solve(A,B):
    hashmap={}
    newHashmap={}
    outputArr=[]

    for i in A:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1

    newHashmap = dict(sorted(hashmap.items(), key=lambda x: x[1]))
    
    for i in deepcopy(newHashmap):
        if newHashmap[i]<=B:
            B-=newHashmap[i]
            newHashmap.pop(i)
        
    return len(newHashmap)


A='bbcbbbccb'
B=2
print(solve(A,B))