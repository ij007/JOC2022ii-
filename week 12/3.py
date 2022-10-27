a = input()
b = a.split('.')

r = b[0].split('@')[0]
i = b[0].split('@')[1]

print(r, i)