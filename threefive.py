def three_five(max_val):
	answer = 0
	for i in range(1,max_val):
		if i%3 == 0 or i%5 == 0:
			answer += i
	return answer
	
def three_five_better(max_val):
	threes = range(0,max_val,3)
	fives = range(0,max_val,5)
	answers = threes + fives
	answers = set(answers)
	return sum(answers)

max = 1000
print(three_five_better(max))