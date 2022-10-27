import math

def closestSchool(x,y, L):
    minD = 1000000
    distance = []
    for i in L:
        x1, y1 = i[0], i[1]
        d = math.sqrt((x1-x)**2 + (y1-y)**2)
        if d<minD:
            distance = []
            distance.append(i)
            minD = d
        elif d == minD:
            distance.append(i)
        
    for i in distance:
        print(i) 