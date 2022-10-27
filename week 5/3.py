L = [int(i) for i in input().split()]
def isprime(num):
    if num<=1:
        return False
    if num==2:
        return True
    
    for i in range(3,num-1):
        if num%i == 0:
            return False
        
    return True

for k in L:
    if isprime(k):
        print(k)
        break
    else:
        continue