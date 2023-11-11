def prime(n):
    if n <=1:
        return False
    if n == 2 or n ==3 or n == 5 or n ==7:
        return True
    if n%2 ==0 or n %3 ==0 or n%5 ==0 or n%7 ==0:
        return False
    else:
        return True

number = 0

while True:
    if prime(number):
        print(number,end=' ')
    
    number += 1
    
     