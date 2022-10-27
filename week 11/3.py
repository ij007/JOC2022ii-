def isPrime(num):
    if num == 2:
        return True
    
    if num<2:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
        
    return True


a = int(input())
b = int(input())

for i in range(a, b+1):
    if not isPrime(i):
        print(i)