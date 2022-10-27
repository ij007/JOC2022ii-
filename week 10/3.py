import string 
import random

upper = string.ascii_uppercase
lower = string.ascii_letters
s = input()
ans = ''
for i in s:
    if i in upper:
        idx = upper.index(i)
        ans += lower[idx]
    elif i in lower:
        idx = lower.index(i)
        ans += upper[idx]
        
    else:
        ans+=i
        
print(ans)