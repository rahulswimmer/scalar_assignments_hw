class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        setB = set(B)
        setC = set(C)
        
        arr = []
        
        for i in A:
            if i in setB:
                arr.append(i)
            elif i in setC:
                arr.append(i)
        
        for i in B:
            if i in setC:
                arr.append(i)
        
        return list(sorted(set(arr)))
        
        
        
        