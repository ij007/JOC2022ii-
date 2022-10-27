def snake(M):
    rowlen = len(M)
    collen = len(M[0])
    ans  = []

    for i in range(rowlen):
        if i%2 == 0:
            for j in M[i]:
                ans.append(j)
        else:
            l = M[i]

            for j in range(-1, -collen-1, -1):
                ans.append(l[j])
    return ans