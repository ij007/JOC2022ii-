n = int(input())
n = str(n)
d = {}
for i in range(len(n)):
    if n[i] not in d.keys():
        d[n[i]] =  [i]
    else:
        d[n[i]].append(i)
        
        
for key, value in d.items():
    print(key, end= ' ')
    for i in value:
        print(i, end= ' ')
        
    print()