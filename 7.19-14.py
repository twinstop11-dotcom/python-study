a,b=map(int,input().split())

for i in range(1,a+1):
    if a%i==0 and b%i==0:
        gcd=i
if gcd==1:
    print('서로소입니다.')
else:
    print('서로소가 아닙니다.')
