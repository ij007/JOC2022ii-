L = [int(i) for i in input().split()]
count = 0
for i in L:
    if i%2 != 0:
        count+=1

print(count)