def solve(A):
    sortedArray = sorted(A)
    start=0
    end=len(A)-1
   
    while start <= end:
        if A[start]==sortedArray[start]:
            start+=1
        else:
            break
    
    while end >= -1:
        print(end)
        if A[end]==sortedArray[end]:
            end-=1
        else:
            break

    return len(A[start:end+1])


A = [ -146316343, 179840175, 760528516 ]
print(solve(A))