def computeSum(n) -> int: 
    sum = 0 

    while n > 0 :
        sum += n
        n -= 1
    return sum

def __main__():
    print(computeSum(10))