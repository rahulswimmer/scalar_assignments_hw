def solve(A):
    count=0
    ans=0
    prefixArr=[0]
    suffixArr=[0 for x in range(len(A))]

    for i in A:
        ans=max(ans,count)
        if i == '1':
            count+=1
        elif i=='0':
            count=0

    for i in range(1,len(A)-1):
        if A[i-1]=="1":
            prefixArr.append(prefixArr[i-1]+1)
        else:
            prefixArr.append(0)
    
    for i in range(len(A)-2,0,-1):
        print(i)
        if A[i+1]=="1":
            suffixArr[i]=suffixArr[i+1]+1
        else:
            suffixArr[i]=0

    print(prefixArr)
    print(suffixArr)
    for i in range(len(A)-1):
        x=prefixArr[i-1]+suffixArr[i+1]
        if x != count:
            ans=max(ans,x+1)
        else:
            if suffixArr[i+1]>0:
                ans=max(ans,prefixArr[i-1]+1)
            elif prefixArr[i-1]>0:
                ans=max(ans,suffixArr[i+1]+1)

    return ans

A="1110111010"
print(solve(A))