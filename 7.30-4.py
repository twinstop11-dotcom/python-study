n=int(input('만드려는 금액을 입력하세요:'))
a=n//7
b=n//17
c=n//27
sum=0
for i in range(0,c+1):
    for j in range(0,b+1):
        for k in range(0,a+1):
            if i*27 + j*17 + k*7==n:
                sum=sum+1
            
if sum==1:
    print('가능합니다.')
else:
    print('불가능합니다.')
