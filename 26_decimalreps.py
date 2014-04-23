def longDiv_iter(divisor, number, max_digits):
    quotient = []
    while len(quotient) < max_digits:
        ans, rem = divmod(number, divisor)
        
        if rem == 0:
            quotient.append(ans)
            return quotient
            
        elif ans == 0:
            quotient.append(0)
            number = number*10
            
        else:
            quotient.append(ans)
            number = rem*10
            
    return quotient       
    
def getUnitDecimals(start, end, rep_length):
    rep = {}
    for i in range(start, end+1):
        rep[i] = longDiv_iter(i, 1, rep_length) 
    return rep
    
def filterDict(mydict, length):
    for k, v in mydict.items():
        if len(v) < length:
            del mydict[k]
    return mydict    
    
def cycleLength(mylist, threshold):
    '''test if a list contains repeating values'''
    maxcyclelen = len(mylist) / threshold
    for i in range(1,maxcyclelen):
        #print "checking if " + str(i) + " values are repeating"
        #get the last i values
        repvals = mylist[-i:]
        #make a copy of mylist for checking vs repvals
        testvals = mylist[:]
        
        check = []
        ok = True
        matches = 0
        
        while (len(testvals) > i) and (ok == True) and (matches <= threshold):
            #populate the values to check vs. repvals
            for k in range(i):
                check.append(testvals.pop())
            check.reverse()
            #if it's a match, keep going    
            if check == repvals:
                check = []
                matches += 1
            #if it's not a match, break out to the next cycle length (i)
            else:
                check = []
                ok = False
                break
        
        if ok == True:
            return i
        else:
            continue
            
    return False
        

def longestRecipCycle(max_val, div_length=10000, mustcycle=3):
    decimalRep = getUnitDecimals(2, max_val, div_length)
    candidates = filterDict(decimalRep, div_length)
    best = (0, 0, [0])
    for k, v in candidates.items():
        c = cycleLength(v,mustcycle)
        if c > best[1]:
            best = (k, c, v)
        else:
            continue
    return best
    


if __name__ == '__main__':
    #a = getUnitDecimals(2,100,20)
    #b = filterDict(a, 20)
    
    #print cycleLength([1,3,3,3,3,3,3,3,3,3,3,3], 3)
    
    print longestRecipCycle(1000)