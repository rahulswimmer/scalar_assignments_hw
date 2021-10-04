def solve(A):
    month=getMonth(A)
    year=getYear(A)
    day=getDay(A)
    return str(year)+"-"+str(day)+"-"

def getDay(A):
    print(A[:2].isalpha())
    return A[0:2]

def getMonth(A):
    months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthHashmap = {}
    month = ""

    for i in range(len(months)):
        monthHashmap[months[i]]=i+1

    if len(str(monthHashmap[A[len(A)-8:7]]))==1:
        month="0"+str(monthHashmap[A[len(A)-8:7]])
    else:
        month=monthHashmap[A[len(A)-8:7]]
    
    return month

def getYear(A):
    return A[len(A)-4:]

A="11th Mar 1984"
print(solve(A))