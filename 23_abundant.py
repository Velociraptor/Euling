# Project euler problem 23
# Eric Jones
# 20 April 2014


def getDivisors(n):
    max_div = n
    poss_div = 2
    divisors = [1, n]
    while poss_div < max_div:
        if n % poss_div == 0:
            divisors.append(poss_div)
            divisors.append(n/poss_div)
            max_div = n/poss_div
        poss_div += 1
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

def getAbundant(max):
    ans = []
    for i in range(1,max):
        divs = getDivisors(i)
        divs.remove(i)
        if sum(divs) > i:
            ans.append(i)
    return ans
    
def getPossibleSums(nums):
    sums = []
    while len(nums) > 0:
        a = nums.pop()
        sums.append(a+a)
        if len(nums) > 0:
            for num in nums:
                sums.append(a+num)
    
    return (list(set(sums)))
    


def otherNums(nums, max):
    i = 1
    others = []
    while i <= max:
        if i not in nums:
            others.append(i)
            i+=1
        else:
            i+=1
    return others
            
    
        
if __name__ == "__main__":
    #Incorrect: 197740174, 197740110
    nums = getAbundant(28123)
    sums = getPossibleSums(nums)
    others = otherNums(sums, 28123)
    print sum(others)
    
    #print sum(others)
    