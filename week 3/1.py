ans = []
for i in L:
    if i%5 == 0 or i%7 == 0 or i%35 == 0:
        ans.append(i)
        
ans.sort()
print(ans)