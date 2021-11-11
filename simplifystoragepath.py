def solve(A):
    outputArr=[]
    B = A.split("/")
    print(B)
    for i in range(1,len(B)):
        print(len(outputArr))
        if B[i]==".." and len(outputArr)!=0:
            outputArr.pop()
        elif B[i]!="." and B[i]!="":
            outputArr.append(B[i])
        
    return "/"+"/".join(outputArr)


A="/../"
print(solve(A))