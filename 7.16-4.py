a,b=map(int,input().split())

if a>b:
    small=b
    big=a
else:
    small=a
    big=b

sum=0
i=small
while i<=big:
     sum=sum+i
     i=i+1
print(sum)
