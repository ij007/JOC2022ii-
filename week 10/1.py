L = list(map(int, input().split()))


m = max(L)
L1 = [0]*(m+1)

for i in L:
    L1[i] = i
    

for i in range(len(L1)-1):
    print(L1[i], end=' ')
    
print(L1[-1])