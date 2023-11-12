# print(" \n hello world")

# x = input()

# print (x)


# def takeNumber ():
#     print("Are You A GUY??")
#     x = input("press y if You ARE ")
#     if x == 'y':
#         input("please Provide your Phone number..")
        
#     else:
#         print ('sorry no girls Are allowed in this moment :(')
        
        
# while True: 
#     takeNumber()
    
d1 = {'a':2, 'b':4, 'c':38}
d2 = {"fruit":["mango","banana"], "flower":["rose", "tulip"]}
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}



##
marklist = {
    "Mahesh" : {"phy": 60, "maths": 70},
    "Boslu" : {"phy": 89, "maths": 69},
    "Bodol": {"phy": 2, "maths": 4},
    "shad": {"phy": 0, "maths": 1}
}

        
        






##lower upper 

data = 'my name is boslu'

print(data.upper())

dataa = 'a'


if dataa.islower():
    print('it is a lower case ')
        
else:
    print ('it is upper case')


##copiying dictionary to another dictionary with a loop

print(capitals.items())

chutiyaLand = {}


for k,v in capitals.items():
    
    chutiyaLand[k] = v
    
print(chutiyaLand)


def absolute(number):
   
   
   
   print('The Absolute NUmbers is ', abs(number))
   
value = int(input('Please Enter a Number'))



absolute(value)
try:
   
   number = float(input('Please enter a number'))

   if isinstance(number,(int,float)):
      print (abs(number))
   
except ValueError:
   print('Only Numbers are accepted\n PLease Enter a number')


def factorial(number):
   
   if number == 0 or number == 1:
      return 1
   else:
      return number * factorial(number -1)
   
n = int(input('please neter a number'))


factorial(n)

