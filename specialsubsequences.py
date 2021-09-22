def solve(A):
    countG=0
    countAG=0

    for i in range(len(A)-1,-1,-1):
        if A[i]=="G":
            countG+=1
        elif A[i]=="A":
            countAG+=countG

    return countAG
A="ABCGAG"
print(solve(A))