s = input()

s_new = ''
vowels = 'aeiouAEIOU'
for i in s:
    if i in vowels:
        s_new+='*'
        
    else:
        s_new+=i
        
print(s_new)