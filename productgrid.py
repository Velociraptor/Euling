import math

def parseline(dict, linenum, line):
    line = line.split()
    for i in range(len(line)):
        dict[ (linenum,i) ] = int(line[i])
        
def parselines(lines):   
    grid = {}
    for (row, text) in lines:
        parseline(grid, row, text)
        
    return grid

def listproduct(list,howmany):
    #max product of lenght howmany from list of ints
    #reutrns 2tuple: (maxproduct, [no1, no2, no3, ...])
    maxproduct = (0, [])
    for i in range(len(list)+1-howmany):
        iszero = False
        theproduct = 1
        thenumbers = []
        for j in range(howmany):
            next = list[i+j]
            if next == 0: 
                iszero = True
                break
            thenumbers.append(next)
            theproduct *= next
        
        if iszero: continue
        if theproduct > maxproduct[0]: maxproduct = (theproduct, thenumbers)
    
    return maxproduct
    
def maxproduct(grid, lists, howmany):
    #max product of len howmany for lists from grid
    runningmax = (0, [])
    
    for list in lists:
        list = [grid[item] for item in list]
        maxp = listproduct(list, howmany)
        if maxp[0] > runningmax[0]: runningmax = maxp
        
    return runningmax
            
    
def multgrid(grid, howmany):
    
    done = False
    max = 0
    lints = []
    
    #Up/Down
    coords = grid.keys()
    coords.sort()      
    coords = [(y,x) for (x,y) in coords] #only for squares
    order = []
    for i in range(len(coords)):
        order.append(coords[i])
        print i
        if (i == len(coords)-1):
            lints.append(order)
            order = []
            break
        if (coords[i][1] != coords[i+1][1]):
            lints.append(order)
            order = []
        
        
    #left/right
    coords = grid.keys()
    coords.sort()
    order = []
    for i in range(len(coords)):
        order.append(coords[i])
        if (i == len(coords)-1):
            lints.append(order)
            order = []
            break
        if (coords[i][0] != coords[i+1][0]):
            lints.append(order)
            order = []
        
    #diagonalley
    order = [] 
    keys = grid.keys()
    keys.sort()
    max = keys[-1]
    
    #right hand diagonals
    next = (1,1)
    for i in range(max[0]-howmany+2):
        pt = (i,0)
        while pt[0] <= max[0] and pt[1] <= max[1]:
            order.append(pt)
            pt = pt[0] + next[0], pt[1] + next[1]
        lints.append(order)
        order = []
        
    for i in range(max[1]-howmany+2):
        pt = (0,i)
        while pt[0] <= max[0] and pt[1] <= max[1]:
            order.append(pt)
            pt = pt[0] + next[0], pt[1] + next[1]
        lints.append(order)
        order = []
        
    #LEFT HAND diagonals!
    next = (-1,1)
    for i in range(max[0]-howmany+2):
        pt = (max[0]-i,0)
        while pt[0] >= 0 and pt[1] <= max[1]:
            order.append(pt)
            pt = pt[0] + next[0], pt[1] + next[1]
        lints.append(order)
        order = []
        
    for i in range(max[0]-howmany+2):
        pt = (max[0],i)
        while pt[0] >= 0 and pt[1] <= max[1]:
            order.append(pt)
            pt = pt[0] + next[0], pt[1] + next[1]
        lints.append(order)
        order = []
            
        
    #AT THIS POINT, ORDER is a list o lists.
    
    maxthing = maxproduct(grid, lints, howmany)
    return maxthing
    
            

            
            
    
ln0 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
ln1 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
ln2 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
ln3 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
ln4 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
ln5 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
ln6 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
ln7 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
ln8 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
ln9 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
ln10 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
ln11 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
ln12 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
ln13 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
ln14 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
ln15 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
ln16 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
ln17 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
ln18 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
ln19 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

lines = [(0, ln0),(1, ln1),(2, ln2),(3, ln3),(4, ln4),
         (5, ln5),(6, ln6),(7, ln7),(8, ln8),(9, ln9),
         (10, ln10),(11, ln11),(12, ln12),(13, ln13),(14, ln14),
         (15, ln15),(16, ln16),(17, ln17),(18, ln18),(19, ln19)]
        
grid = parselines(lines)
print multgrid(grid, 4)