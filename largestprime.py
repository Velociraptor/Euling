import math

def largestprime(value):
	maxhalf = int(math.ceil(value/2.0))
	quickness = 1000000
	quickprimes = makeprimes(3,quickness)
	quickprimes.reverse()
	for prime in quickprimes:
		if value%prime == 0:
			maxhalf = value/prime
			break
			

	testprimes = makeprimes(quickness,maxhalf)
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

# print makeprimes(100)
# print largestprime(600851475143)
print largestprime(13195)