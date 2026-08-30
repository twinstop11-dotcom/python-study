d={}


while True:
    a=int(input())
    if a==-1:
        break
    else:
        sum=0
        for i in range(1,a+1):
            if a%i==0:
                sum=sum+1
        d[a]=sum
print(d)
                                                      
