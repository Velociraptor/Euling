def evenfibsum(max_val):
	numbers = []
	evensum = 0
	first = 1
	second = 1
	numbers.append(first)
	numbers.append(second)
	while numbers[-1] < max_val:
		numbers.append(numbers[-1] + numbers[-2])
		if numbers[-1]%2 == 0:
			evensum += numbers[-1]
			
	if numbers[-1]%2 == 0:
		evensum -= numbers[-1]
	
	return evensum	
	
print(evenfibsum(4000000))
	