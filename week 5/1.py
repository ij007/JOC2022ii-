def count_letters(S):
    d={}
    for i in S:
        d[i]=0
    for i in S:
        d[i]+=1
    return d