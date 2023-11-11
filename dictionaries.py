d1 = {'a':2, 'b':4 , 'c': 38}

k1 = ['b','c']

dt = {}

d2 = {"fruit":["mango", "banana"], 'flower': ['rose', 'tulip']}

capitals= {"maharashtra":"mumbai", "gujarat":"Gandhinagar","Telangana":"Hyderabad", "Karnataka":"Bengaluru"}

marklist = {
    "Mahesh" : {"phy": 60, "maths": 70},
    "Boslu" : {"phy": 89, "maths": 69},
    "Bodol": {"phy": 2, "maths": 4},
    "shad": {"phy": 0, "maths": 1}
}


# # # adding two dictionaries
# d3 = d1|d2
# print(d3)

# # augmenting two dictionaries in one 

# d1|=d2
# print(d1)


# # # finding a value in a dictionary using key 

# value = d1["a"]

# print(value)

# # #  (***CRUD ) getting dictionary value adding a string in between nested dictionaries

# value = ' and ' .join(d2.get('flower'))
# print(value)

# # # (**CRUD) getting values by keyin a dictionary 

# cap = capitals.get('maharashtra')
# print(cap)

# # # (**CRUD) Adding a new key valur pair 

# capitals.update({'Bangladesh': 'Dhaka'})

# print(capitals)

# # # (**CRUD) popping key value by key it will remove both key & value  

# capitals.pop('maharashtra')

# print(capitals)

# # # (**CRUD)using DEL key valu p[air can also be deleted using the del function 

# del capitals['gujarat']

# print(capitals)

# # # make an object of a dictionary callint dictionary.items()
# # # keeping inside the type function it will tell its type as dictionary items

# obj = d1.items()

# print(obj)

# print(type(obj))


# # # # # manipulating  dictionary data as dictionary object
# # # finding keys values & items 
# k = d1.keys()
# print(k)

# v = d1.values()

# print(v)

# i = d1.items()

# print(i)


###############Python program to create a new dictionary by extracting the keys 
############# from a given dictionary.

# for i in k1:
    
#     dt[i] = d1[i]
    
 
# print(dt)    

# ###############Python program to convert a dictionary to list of (k,v) tuples.

# l = d1.items()
# t = list(l)

# print(t)

##### Python program to remove keys with same values in a dictionary.

# d5 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}

# l = list(d5.values())

# val = [x for x in l if l.count(x)==1]

# print(val)

# for k,v in d5.items():
#     if v in val:
        
#         d = {k:v}
#         dt.update(d)
        
# print(dt)

# # # looping though dictionary 

# for keys 

# for x in d1:
#     print(x, end= ' ')

# print('\n')
# # for values
# for v in d1.values():
#     print(v, end=' ')
# print('\n')

# ###### for key pair value from items()

# for k,v in d1.items():
#     print(k, ':' , v)


########## for key pair value just from keys 

# for x in d1.keys():
#     print(x,':', d1[x])

# print(len(d1))

# l = len(d1)

# ## #keys and values and dict key and dict values are at the same index

# for x in range(l):
#     print(list(d1.keys())[x],':' ,list(d1.values())[x] )
    
        
#####nested stuff 

# for x,y in marklist.items():
    
#     print(x, ':', y)
    
    
    
v = marklist.get('shad')['phy']

print(v)

w = marklist["Boslu"].get('maths')
print(w)