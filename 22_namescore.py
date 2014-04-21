# Project euler problem 22
# Eric Jones
# 20 April 2014


def sortNames(fname='names.txt'):
    data = []
    fin = open(fname)
    for line in fin:
        split = line.split(',')
        for name in split:
            name = name[1:-1]
            data.append(name)
    data.sort()
    return data
    
def scoreName(name):
    a = [ord(x)-64 for x in name]
    return sum(a)
    
def scoreNamesInList(name_list):
    name_list.reverse() #because pop() takes the last item.
    idx = 1
    scores = []
    while len(name_list) > 0:
        score = scoreName(name_list.pop())
        scores.append(score*idx)
        idx+=1
    return sum(scores)
    
        
    
if __name__ == '__main__':
    names_in_order = sortNames()
    print scoreNamesInList(names_in_order)