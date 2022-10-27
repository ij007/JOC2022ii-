L = [int(i) for i in input().split()]
d = {}

for i in range(len(L)):
    if L.count(L[i]) >= 2:
        if L[i] not in d.keys():
            d[L[i]] = [i]
        else:
            d[L[i]].append(i)
            
print(d)