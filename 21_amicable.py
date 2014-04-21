# Project euler problem 21
# Eric Jones
# 20 April 2014

import math

def d(n):
    divs = getDivisors(n)
    divs.remove(n)
    return sum(divs)

def getDivisors(n):
    max_div = n
    poss_div = 2
    divisors = [1, n]
    while poss_div < max_div:
        if n % poss_div == 0:
            divisors.append(poss_div)
            divisors.append(n/poss_div)
            max_div = n/poss_div
        poss_div += 1
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

def findAmicable(max):
    a = 2
    amicable = {}
    while a < max:
        try:
            if amicable[a][1] == True: 
                pass
        except:
            d_a = d(a)
            d_b = d(d_a)
            if a == d_b and a != d_a:
                amicable[a] = (d_a, True)
                amicable[d_a] = (a, True)
                #print "Amicable: ", a, d_a
            else:
                amicable[a] = (0, False)
        a += 1  
    return amicable
    
def sumAmicable(max):
    amicables = findAmicable(max)
    sum = 0
    for (n, b) in amicables.values():
        if b:
            sum += n
    return sum
    
    
if __name__ == "__main__":
    print sumAmicable(10000)