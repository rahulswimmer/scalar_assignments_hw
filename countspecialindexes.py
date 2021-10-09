def solve(A):

    # below code is tc o(n) and sc o(n)
    # prefixSumOddArr = [0 for i in range(len(A))]
    # prefixSumEvenArr = [0 for i in range(len(A))]

    # for i in range(len(A)):
    #     prefixSumOddArr[i]=prefixSumOddArr[i-1]
    #     prefixSumEvenArr[i]=prefixSumEvenArr[i-1]
    #     if i%2!=0:
    #         prefixSumOddArr[i]+=A[i]
    #     else:
    #         prefixSumEvenArr[i]+=A[i]
   
    # for i in range(len(A)):
    #     if prefixSumOddArr[i-1]+prefixSumEvenArr[len(A)-1]-prefixSumEvenArr[i]==prefixSumOddArr[len(A)-1]-prefixSumOddArr[i]+prefixSumEvenArr[i-1]:
    #         return i

    # below code is tc o(n) and sc o(1)
    leftOdd,leftEven = 0,0
    rightOdd, rightEven = 0,0
    ans=0

    for i in range(len(A)):
        if i%2!=0:
            rightOdd+=A[i]
        else:
            rightEven+=A[i]
    
    for i in range(len(A)):
        if i%2!=0:
            rightOdd-=A[i]
        else:
            rightEven-=A[i]

        if leftOdd+rightEven==leftEven+rightOdd:
            ans+=1

        if i%2!=0:
            leftOdd+=A[i]
        else:
            leftEven+=A[i]
    return ans

A=[2,1,6,4]
print(solve(A))