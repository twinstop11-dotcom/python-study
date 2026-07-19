a=int(input())
sum=0
i=1
while i<=a:
    if a%i==0:
        sum=sum+1
    i=i+1
if sum>2:
    print('소수가 아닙니다.')
else:
    print('소수 입니다.')
    
