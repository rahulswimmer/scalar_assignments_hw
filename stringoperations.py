def solve(A):
    arr=[]
    for i in A+A:
        if not i.isupper():
            arr.append(i)
    
    for i in range(0,len(arr)):
        if arr[i]=='a' or arr[i]=='e' or arr[i]=='o' or arr[i]=='i' or arr[i]=='u':
            arr[i]='#'

    return "".join(arr)

A='AbcaZeoB'
print(solve(A))