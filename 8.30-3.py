d={'소수':[],'합성수':[]}

while True:
    a=int(input())
    if a==-1:
        break
    else:
        sum=0
        for i in range(1,a+1):
            if a%i==0:
                sum=sum+1
        if sum==2:
            d['소수'].append(a)
        else:
            d['합성수'].append(a)

print(d)
