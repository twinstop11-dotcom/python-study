a=int(input())
sum=0
while a>0:
    if a%10==3 or a%10==6 or a%10==9:
        sum=sum+1
    a=a//10
print(sum)
