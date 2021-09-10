def solve(A):
    countOccurences=0
    for i in range(0,len(A)-2):
        if(A[i]+A[i+1]+A[i+2]=="bob"):
            print(A[i]+A[i+1]+A[i+2])
            countOccurences+=1
    return countOccurences

A="3ddsadsdboboboboboboa"
print(solve(A))