def solve(A):
    A = A.split(" ")
    return str("".join(A[2]))+"-"+str(getMonth(A[1]))+"-"+str(getDay(A[0]))

def getDay(A):
    if len(A)==3:
        return "0"+"".join(A[0])
    return A[0:2]

def getMonth(A):
    months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthHashmap = {}

    for i in range(len(months)):
        monthHashmap[months[i]]=i+1

    if len(str(monthHashmap[A]))==1:
        return "0"+str(monthHashmap[A])
    return monthHashmap[A]

A="25th Apr 2217"
print(solve(A))