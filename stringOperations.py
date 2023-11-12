data = 'i want to Play Dota 2 so bad, i cant play right now'
li =['w', 'o', 'r', 'l', 'd']

# # capitralize

l = data.capitalize()

print(l)


# # lower 


l = data.lower()

print(l)


# # # upper 

l = data.upper()
print(l)

# # # list to string 

st = ''.join(li)

print(st)

# # # # string to list 


print(list(st))

# # # inserting in list 

li.append('s')

print(li)

li.insert(2,'x')
print(li)

# # # # # string split 

print(data.split(' '))


# # 3 # # # # find 

print(data.find("Dota"))

# # # count can only count the times a character is used 

co = data.count('i')

print(co)

# # # # # replace must assign a variable first 
newData = data.replace('play','ride')

print(newData)