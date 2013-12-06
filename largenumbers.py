def read_numbers(file_in):
    numbers = []
    for line in file_in:
        #print line
        number = int(line[:-1])
        numbers.append(number)
    return numbers
    
numbers = read_numbers(open('largenumbers.csv','r'))
print sum(numbers)