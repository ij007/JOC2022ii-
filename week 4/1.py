n = int(input())
k = int(input())

l = [0]*n
if k%2 == 0:
    for i in range(len(l)):
        if i%2==0:
            l[i] = 1
            
else:
    for i in range(len(l)):
        if i%2!=0:
            l[i]=1

print(l)