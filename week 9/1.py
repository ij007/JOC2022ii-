def subStr(s1, s2):
    M = len(s1)
    N = len(s2)
 

    for i in range(M - N + 1):
        flag = True
        for j in range(N):
            if (s1[i + j] != s2[j]):
                flag = False
                break
             
        if flag :
            return True
 
    return False