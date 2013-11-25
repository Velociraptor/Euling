def check_pal(val):
    stringed = str(val)
    for i in range(len(stringed)/2):
        if stringed[i] != stringed[-i-1]:
            return False
    return True

def make_numbers(length):
    numbers = []
    min_thing = int('1'+'0'*(length-1))
    max_thing = int('9'*length)
    for i in range(min_thing,max_thing+1):
        numbers.append(i)
    return numbers
    
def multiply_things(numbers):
    pals = []
    for i in range(1,len(numbers)-1):
        number1 = numbers[-i]
        for j in range(1,len(numbers)-1-i):
            number2 = numbers[-j]
            
            thing = number1*number2
            if check_pal(thing):
                pals.append(thing)
    return max(pals)

numbers = make_numbers(3)
print multiply_things(numbers)

