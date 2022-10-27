import copy 

L = input().split()
temp = []
for i in L:
    a = list(i)
    a.reverse()
    a = ''.join(a)
    temp.append(a)
    

temp.sort()
l = copy.deepcopy(temp)
temp = []

for i in l:
    a = list(i)
    a.reverse()
    a = ''.join(a)
    temp.append(a)

print(temp)