def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        f = n * factorial(n-1)
        
        return f
        
number = int(input('please insert a number'))


factorial(number)