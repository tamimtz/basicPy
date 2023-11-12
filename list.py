#list operations 


li = [4,3,'two','one']
#list add

num = li+li

print (num)

#list multiply 

mul = li * 3
print(mul)

#check in list membership

if 3 in li:
   print('3 is in list')


#$finding through index

obj = li[2]
print(obj)

#find from a range of index

obj = li[0:3]

print(obj)

#appen or insert new otem 
li.append('5')

print(li)

#insert new item with an index 

li.insert(2, 'seven')
print(li)

#insert last item = append (incase if you are dumb enough to think -0 would work)

#removing items with list item

li.remove(3)
print(li)

#removing using pop

li.pop(1)
print(li)


#also can use del like in the dictionary
#but here use value instead of a key


del li[0]

print(li)


for x in li:
   print(x, end= ' ')


#  #  #  # looping in the list 

lst = [ 25, 43, 67, 87, 57]

numlst = range(len(lst))


for i in numlst:
   print("lst[{}]:" .format(i), lst[i])
   
chars ='i love bangladesh'

char = [c for c in chars if c not in 'aeiou']

print(char)
    
    
# # # # list sorting 
ort = ['bangla', 'English', 'arabic', 'arameic']
ort.sort(key=str.lower)
print(ort)