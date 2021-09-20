def solve(A):
    str1=''
    outputArr=[]
    for i in A:
        str1+=str(i)
    
    str1 = str(int(str1)+1)
    
    for i in str1:
        outputArr.append(i)

    return outputArr

A=[3,6,7]
print(solve(A))