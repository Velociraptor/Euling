def specialpythag(sum):
    for a in range(1,sum):
        for b in range(a+1,sum-a):
            c = sum - a - b
            if c <= b: continue
            
            triplet = (a,b,c)
            a2 = a*a
            b2 = b*b
            
            if a2 + b2 <= c: continue
            c2 = c*c
            if a2+b2 == c2:
                print triplet
                ans = triplet[0]*triplet[1]*triplet[2]
                return ans
                
    return "no pythagoran triplets with this sum"
            
            
# print specialpythag(7+24+25)
print specialpythag(1000)