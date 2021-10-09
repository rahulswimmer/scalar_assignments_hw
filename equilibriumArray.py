from abc import abstractproperty


def solve(A):
    # prefixArr = []
    # suffixArr=[]
    # count=0
    # for i in range(len(A)):
    #     if i == 0:
    #         prefixArr.append(A[0])
    #     else:
    #         prefixArr.append(A[i]+prefixArr[i-1])

    # for i in range(len(A)-1,-1,-1):
    #     if i == len(A)-1:
    #         suffixArr.append(A[len(A)-1])
    #     else:
    #         suffixArr.append(A[i]+suffixArr[count-1])
    #     count +=1
    # count=0
    # return prefixArr,suffixArr

    sumArray=sum(A)
    leftSum=0

    for i in range(len(A)):
        sumArray -= A[i]

        if leftSum == sumArray:
            return i
        leftSum += A[i]
    return -1

    

A=[-7, 1, 5, 2, -4, 3, 0]
print(solve(A))