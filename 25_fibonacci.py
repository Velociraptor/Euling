def fib(des_digits):
    fibs = [1,1]
    while len(str(fibs[-1])) < des_digits:
        fibs.append(fibs[-2]+fibs[-1])
    return len(fibs)
        
if __name__ == '__main__':
    print fib(1000)