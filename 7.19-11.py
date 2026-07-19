a=int(input())
sum=0

for i in range(1,a+1):
    if a%i==0:
        sum=sum+1
    i=i+1
if sum>2:
    print('소수가 아닙니다.')
else:
    print('소수입니다.')
