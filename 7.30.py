n=int(input())
sum=0
for i in range(1,n+1):
    while i>0:
        if i%10==3 or i%10==6 or i%10==9:
            sum=sum+1
        i=i//10
print(sum)
