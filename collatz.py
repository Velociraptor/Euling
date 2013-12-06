def makecollatz(number, seq):
    if number == 1:
        seq.append(number)
        return seq
    else:
        seq.append(number)
        if number % 2 == 0:
            return makecollatz(number/2, seq)
        else:
            return makecollatz(3*number+1, seq)

# print len(makecollatz(27, []))
# print makecollatz(13,[])
start = [[1], [2]]
def collatzbackward(list):
    answers = range(3,1000001)
    nums = [num for sublist in list for num in sublist]
    collatzs = set(nums)
    while len(answers) > 10:
        
        starts = list[-1]
        new = []
        for item in starts:
            a = item*2
            b = (item-1) / 3.0
            if a not in collatzs:
                new.append(a)
                try: 
                    answers.pop(answers.index(a))
                except:
                    pass
                
            if (int(b) == b) and (b not in collatzs):
                new.append(int(b))
                try: 
                    answers.pop(answers.index(int(b)))
                except:
                    pass
        list.append(new)
        nums = [num for sublist in list for num in sublist]
        collatzs = set(nums)
        print len(list), len(answers)
        if len(answers) < 500:
            print answers
    return answers

print collatzbackward(start)


# memo = {1:[1]}
# def collatz(number, memo):
    # seq = []
    # if number in memo.keys():
        # return memo[number]
    # else:
        # seq.append(number)
        # if number % 2 == 0:
            # thing = seq + collatz(number/2, memo)
            # memo[number] = thing
            # return thing
        # else:
            # thing = seq + collatz(3*number+1, memo)
            # memo[number] = thing
            # return thing
            
            
# longest = (-1, -1)
# for i in range(1, 1000000):
    # seq = collatz(i, memo)
    # seqlength = len(seq)
    # if seqlength > longest[0]:
        # longest = (seqlength, i)
        # print longest
    # # print memo.items()
    
    
    