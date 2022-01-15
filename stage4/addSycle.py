n = int(input())
oringinalN = n
result = 0

while 1:
    if n <10 and n >= 0:
        result = result +1
        faken = str(n) + str(n)
        n = int(faken)
        
    elif n<100 and n >= 0:
        result = result +1
        a = str(n)
        b = int(a[0]) + int(a[1])
        c = str(b)
        f = int(c)
    
        if f < 10:
            d = a[1] + c[0]
    
        else:
            d = a[1] + c[1]
    
        n = int(d)
    
        if oringinalN == n:
            print(result)
            break
        
        break
    
    else:
        break