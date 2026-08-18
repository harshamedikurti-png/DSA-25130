def fact(n): 
    if n==0:
        return 1 
    elif n==1: 
        return 1
    else:
        return n*fact(n-1)
n = int(input('Get me the number for Factorial calculate:\t')) 
print(f'Factorial of {n} is {fact(n)}')
