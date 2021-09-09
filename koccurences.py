def getSum(A, B, C):
    hashmap = {}
    sum=0
    for i in C:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] =1
    ok=False
    for i in hashmap:
        if hashmap[i]==B:
            sum+=i
            ok=True
    if ok==False: return -1
    return sum

C=[0,0,1]
A=len(C)
B=2
print(getSum(A,B,C))