def gcd(a,b):
    cnt=0
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            cnt=i
    return cnt
            
            

    
    
