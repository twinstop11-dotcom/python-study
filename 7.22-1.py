a,b=map(int,input().split())

if a>b:
    small=b
    big=a
else:
    small=a
    big=b

sum1=0
sum2=0
sum3=0

for i in range(small,big+1):
    if i%7==0:
        sum1=sum1+1
    if i%17==0:
        sum2=sum2+1
    if i%17==0 and i%7==0:
        sum3=sum3+1
print(f'짱수: {sum1}개')
print(f'짱짱수: {sum2}개')
print(f'짱짱짱수: {sum3}개')

    
