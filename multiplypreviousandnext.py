def solve(A):
        outputArr = []
        if len(A)==1: return A
        for i in range(len(A)):
            print(i)
            if i==0:
                outputArr.append(A[i]*A[i+1])
            elif i==len(A)-1:
                outputArr.append(A[i-1]*A[i])
            else:
                outputArr.append(A[i-1]*A[i+1])
        return outputArr

A=[0]
print(solve(A))