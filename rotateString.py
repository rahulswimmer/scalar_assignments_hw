def solve(A,B):
    outputArr=[]
    for i in A:
        outputArr.append(i)
    
    n = outputArr[0]
    
    if B>len(outputArr): B=B%len(outputArr)

    start=0
    end=len(outputArr)-1
    while start < end:
        temp=A[start]
        outputArr[start]=outputArr[end]
        outputArr[end]=temp
        start+=1
        end-=1
  
    start=0
    end=B-1
    while start < end:
        temp=outputArr[start]
        outputArr[start]=outputArr[end]
        outputArr[end]=temp
        start+=1
        end-=1

    start=B
    end=len(outputArr)-1
    while start < end:
        temp=outputArr[start]
        outputArr[start]=outputArr[end]
        outputArr[end]=temp
        start+=1
        end-=1

    return "".join(outputArr)

A="scaler"
B=3
print(solve(A,B))