def solve(A):
    outputArr=[]
    outputArr.append(A[0])

    isPreviousNumberEven=checkEven(outputArr[0])

    for i in range(1,len(A)):
        isPreviousNumberEven=checkEven(outputArr[len(outputArr)-1])
        if checkEven(A[i]):
            if not isPreviousNumberEven and A[i]!=outputArr[len(outputArr)-1]:
                outputArr.append(A[i])
        else:
            if isPreviousNumberEven and A[i]!=outputArr[len(outputArr)-1]:
                outputArr.append(A[i])

    return len(outputArr)

def checkEven(n):
    if n%2==0: return True
    else: return False

A = [ 12, 10, 28, 37, 43, 40, 14, 12, 48 ]
print(solve(A))
