a=int(input())
b=a//7
sum=0
for i in range(0,b+1):
    c=a-7*i
    if c%17==0:
        sum=1
if sum==1:
    print('만들 수 있습니다.')
else:
    print('만들 수 없습니다.')
    
        
    
    

