def uniqueE(L):
    d = {}
    for i in L:
        d[i]=0
    for i in L:
        d[i]+=1
            
    res = []
    for key, value in d.items():
        if value==1:
            res.append(key)
            
    res.sort()
    return res