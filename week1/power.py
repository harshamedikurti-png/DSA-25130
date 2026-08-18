def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n1) 


p=float(input('get me the amount:\t')) 
n=int(input('agreed years:\t')) 
print(power(p,n))
