a=input()
sum=0
cnt=0
score=0

if ord(a[0])>=ord('A') and ord(a[0])<=ord('Z'):
    sum=sum+1

if len(a)>=10 and len(a)<=20:
    sum=sum+1

for i in a:
    if ord(i)>=ord('a') and ord(i)<=ord('z'):
        score=score+1
    if ord(i)>=ord('0') and ord(i)<=ord('9'):
        cnt=cnt+1
if score>=3 and cnt>=3:
    sum=sum+1


if sum==3:
    print('조건에 부합합니다.')
else:
    print('조건에 부합하지 않습니다.')

    

    
