import math

def sumsquares(max):
    #computes the sum of squares from 1 to max
    sum = 0
    for i in range(1,max+1):
        sum += i**2
    return sum
        
def squaresum(max):
    #sums 1 to max, and squares that value
    value = sum(range(1,max+1))
    return value**2
    

# print sumsquares(10)
print sumsquares(100)
print squaresum(100)
print squaresum(100) - sumsquares(100)