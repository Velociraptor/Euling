import math

def factor(value,factors):
    print value, factors
    if value in someprimes:
        factors.append(value)
        factors.sort
        print value, factors
        return factors[-1]

    else:
        for prime in someprimes:
            if value%prime == 0:
                newvalue = value/prime
                factors.append(prime)
                return factor(newvalue, factors)
        print 'no more primes under 1000000'
        return 

def largestprime(value):
    maxhalf = int(math.ceil(value/2.0))
    quickness = 1000000
    quickprimes = makeprimes(3,quickness)
    for prime in quickprimes:
        if value%prime == 0:
            maxhalf = value/prime
            print maxhalf, 'divider:', prime
            break
    
    testprimes = makeprimes(quickness,maxhalf+1)
    testprimes = quickprimes + testprimes
    testprimes.reverse()
    for prime in testprimes:
        if value%prime == 0:
            maxprime = prime
            break
    
    return maxprime
    
def makeprimes(start, max_val):
    primes = [2]
    i=start
    while i < max_val:
        root = math.sqrt(i)
        isprime = True
        for prime in primes:
            if prime > root:
                #no dividing primes greater than root(i)
                break
            if i%prime == 0:
                #prime divides -> not prime
                isprime = False
                break
        
        if isprime:
            primes.append(i)
        
        i += 1
    return primes



someprimes = makeprimes(3,1000000)
# print factor(13195,[])
# print factor(600851475143, [])

print someprimes[10000]

# primes = makeprimes(3,int(math.ceil(13195/2.0)))
# primes.reverse()
# for prime in primes:
    # if 13195%prime == 0:
        # print prime
        # break