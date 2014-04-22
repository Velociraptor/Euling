# Project euler problem 24
# Eric Jones
# 22 April 2014

from itertools import permutations as permute 

if __name__ == '__main__':
    a = [0,1,2,3,4,5,6,7,8,9]
    z = permute(a) #z is an itertools object
    z = [x for x in z]
    z.sort()
    print z[1000000-1]