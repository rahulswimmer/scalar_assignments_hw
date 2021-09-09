def solve(A):
    outputArr=[]
    for i in A:
        if ((ord(i) in range(65,91)) or (ord(i) in range(97,123)) and i.islower()):
            outputArr.append(i.upper())
        else:
            outputArr.append(i)
    return outputArr

A="ScalarAcademy##"
print(solve(A))