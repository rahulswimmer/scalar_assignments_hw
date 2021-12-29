class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A,B):
        #A.sort()
        minNum = min(A)
        maxNum = max(A)
        
        hm={}
        for i in range(len(A)):
            if A[i] in hm:
                hm[A[i]]+=1
            else:
                hm[A[i]]=1
                
        while minNum < maxNum:
            minf = hm[minNum]
            maxf = hm[maxNum]
            
            if minf < maxf:
                if B >= minf:
                    B-=minf
                    minNum+=1
                    if minNum in hm:
                        hm[minNum]+=minf
                    else:
                        hm[minNum]=minf
                else:
                    break
            else:
                if B >= maxf:
                    B-=maxf
                    maxNum-=1
                    if maxNum in hm:
                        hm[maxNum]+=maxf
                    else:
                        hm[maxNum]=maxf
                else:
                    break
        return maxNum-minNum
