def fib(n):
    
    n1 = 0
    n2 = 1
    count = 1
    if n == 0:
        return 0
    if n > 0:
        
        while count < n:
        
            nth = n1 + n2
            n1 = n2
            n2 = nth
        
            count = count + 1
        return n2
    else:
        n = n * -1
        while count < n:
            
        
            nth = n1 + n2
            n1 = n2
            n2 = nth
        
            count = count + 1
        if n % 2 == 0:
            
            return n2 * -1
        else:
            return n2
        
print(fib(1))