def make_triangles(howmany):
    triangles = []
    triangle = 0
    for i in range(howmany):
        triangle += i+1
        triangles.append(triangle)
    return triangle
        
#triangles = {1:1}
def make_recursive_triangles(last, triangles):
    try:
        return triangles[last]
    except:
        triangle = last + make_recursive_triangles(last-1,triangles)
        triangles[last] = triangle
        return triangle

#print make_triangles(10)
#print make_recursive_triangles(10, triangles)

def get_divisors(number):
    maxdiv = number
    poss_div = 2
    divisors = [1, number]
    while poss_div < maxdiv:
        if number % poss_div == 0:
            divisors.append(poss_div)
            divisors.append(number/poss_div)
            maxdiv = number/poss_div
        poss_div += 1
    return len(set(divisors))
    
#print get_divisors(49)

triangles = {1:1}
def triangle_div(divisors):
    divs = 0
    last = 1
    while divs < divisors:
        tri = make_recursive_triangles(last, triangles)
        divs = get_divisors(tri)
        last += 1
        #print [tri, divs]
    return tri

print triangle_div(500)