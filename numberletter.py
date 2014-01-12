ones = {1:"one",
		2:"two",
		3:"three",
		4:"four",
        5:"five",
        6:"sex",
        7:"seven",
        8:"eight",
        9:"nine",
        0:"",
        }
teens = {10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        }
tens = {2:"twenty",
        3:"thirty",
        4:"forty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety",
        0:"",
		}
hunds = ones        


totalchars = 0      
for i in range(1,100):
    if i < 10:
        totalchars += len(ones[i])
        print "ones", i
    elif i < 20:
        print "teens", i
        totalchars += len(teens[i])
    elif i < 100:
        print i
        digits = str(i)
        tenschars = len(tens[int(digits[0])])
        oneschars = len(ones[int(digits[1])])
        totalchars += tenschars + oneschars
        
actuallytotalchars = totalchars
for j in range(1,10):
    actuallytotalchars += ((len(hunds[j]) + len("hundred"))) * 100 + (len("and") * 99) + totalchars
    
actuallytotalchars += len("onethousand")

print actuallytotalchars