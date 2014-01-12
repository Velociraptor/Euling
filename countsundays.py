def sundaysinyear(DoW,leap):
    '''compute day number of all sundays for a year, given
    start of year DoW (M:1,T:2,W:3,R:4,F:5,S:6,U:7) and leap T/F'''
    
    firstU = 8-DoW
    if not leap:
        sundays = range(firstU,366,7)
    if leap:
        sundays = range(firstU,367,7)
    return sundays

def isleap(year):
    '''compute if leap year or not'''
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True

def isfirstofmonth(day,leap):
    '''compute if a given day number is a first of the month'''
    firsts = (1,32,60,91,121,152,182,213,244,274,305,335)
    leapfirsts = (1,32,61,92,122,153,183,214,245,275,306,336)
    if not leap:
        if day in firsts:
            return True
    if leap:
        if day in leapfirsts:
            return True
            
    return False
    
def nextyearDoW(sundays,leap):
    '''DoW (M:1,T:2,W:3,R:4,F:5,S:6,U:7)'''
    lastU = sundays[-1]
    if not leap:
        DoW = 366-lastU
    if leap:
        DoW = 367-lastU
        
    return DoW
    
    
def countfirstsundays(year, startDoW):
    '''do it'''
    leap = isleap(year)
    sundays = sundaysinyear(startDoW,leap)
    nextDoW = nextyearDoW(sundays,leap)
    firstsundaysct = 0
    for day in sundays:
        if isfirstofmonth(day,leap):
            firstsundaysct += 1
    return firstsundaysct, nextDoW

DoWtable = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
allfirstUs = 0
startDoW = 1 #January 1, 1900 was a Monday.
for year in range(1900,2001):
    print year, DoWtable[startDoW]
    count, next = countfirstsundays(year, startDoW)
    if year != 1900: #Asks for 1901 through end of 2000
        allfirstUs += count
    startDoW = next
    
print allfirstUs
    