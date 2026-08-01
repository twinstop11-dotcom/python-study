a=int(input())

b=2
sum=0

for b in range(2,a+1):
    sum=0
    for i in range(1,b+1):
   
        if b%i==0:
            sum=sum+1
    
    if sum==2:
        
        c=a-b
        sum=0

        for i in range(1,c+1):
            if c%i==0:
                sum=sum+1

        if sum==2:

            print(f'{a} = {b} + {c}')
            break
           
