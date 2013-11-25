import math

def smallest_mult(maxdiv):
    num = maxdiv
    dividers = range(1,maxdiv+1)
    dividers.reverse()
    while num <= math.factorial(maxdiv):
        divided = True
        for div in dividers:
            if num%div != 0:
                divided = False
                break
        
        if divided:
            return num
        
        num += maxdiv


    
print smallest_mult(20)
    
