def DiagCalc(M):
    countL = 0
    countR = 0
    for i in range(len(M)):
        countL += M[i][i]
        countR += M[i][-1 - i]

    print(countL)
    print(countR)

