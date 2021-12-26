import sys  

def findminxor(A):
    ans =  int(sys.float_info.max)
    val = 0
    A.sort()
    
    for i in range(len(A)-1):
        val = A[i] ^ A[i + 1];
        ans = min(ans, val);
    
    return ans


A=[12,4,6,2]
print(findminxor(A))