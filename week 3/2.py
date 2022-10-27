def rev(L, n):
    L.sort()
    L.reverse()
    print(L[:n])

n = int(input())
L = [int(i) for i in input().split()]
rev(L, n)