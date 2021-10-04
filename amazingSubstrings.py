def solve(A):
    ans=0
    for i in range(len(A)):
        if A[i]=='a' or A[i]=='e' or A[i]=='A[i]' or A[i]=='o' or A[i]=='u' or A[i]=='A' or A[i]=='E' or A[i]=='I' or A[i]=='O' or A[i]=='U':
            ans += len(A)-i
    return ans%10003

A="pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"
print(solve(A))