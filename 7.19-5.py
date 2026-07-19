a,b=map(int,input().split())
if a<b:
    small=a
    big=b
else:
    small=b
    big=a
sum=0
for i in range(small,big+1):
    sum=sum+i
print(sum)
