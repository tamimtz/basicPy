## finding vowels 

text = 'i love bangladesh'

vchars = []

for i in text:
    if i in 'aeiou':
        vchars.append(i)


print(chars)


#### finding consonents 
cChars = []

for i in text:
    if i not in 'aeiou':
        cChars.append(i)
        

print(cChars)