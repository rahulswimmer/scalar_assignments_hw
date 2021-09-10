def solve(A):
    splitArr = A.split(sep=" ")
    outputArr=[]
    for i in range(len(splitArr)-1,-1,-1):
        outputArr.append(splitArr[i])
    return ' '.join(outputArr)

A='this is my life'
print(solve(A))