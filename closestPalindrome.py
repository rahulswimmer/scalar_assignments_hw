def solve(A):
    count=0
    start=0
    end=len(A)-1

    while start <= end:
        if A[start]!=A[end]:
            count +=1
        start+=1
        end-=1
    
    if count == 1:
        return "YES"
    elif count == 0 and len(A)%2 !=0:
        return "YES"
    else:
        return "NO"


A='aba'
print(solve(A))