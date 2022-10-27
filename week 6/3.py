s = input()

s = s.lower()

temp = s[::-1]

if s == temp:
    print('palindrome')
    
else:
    print('not palindrome')