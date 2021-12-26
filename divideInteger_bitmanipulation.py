
def divide(A, B):
    sign = (-1 if((A < 0) ^
                  (B < 0)) else 1);
     
    A = abs(A);
    B = abs(B);
     
    ans = 0;
    temp = 0;
     
    for i in range(31, -1, -1):
        if (temp + (B << i) <= A):
            temp += B << i;
            ans |= 1 << i;
   
    if sign ==-1 :
      ans=-ans;
    return ans;

A=-2147483647
B=-1
print(divide(A,B))