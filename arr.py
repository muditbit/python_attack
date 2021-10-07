import math

n = int(input())
m = int(input())
p = math.log(n)/math.log(m)
a = pow(m,math.floor(p))
b = a*m
if b-n<=n-a:
    ans=b
else:
    ans =b

print(ans)
