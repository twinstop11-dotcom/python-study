n=int(input())
sum=0
for i in range(2,n+1):
    for j in range(1,i):
        sum=sum+j/i
print(sum)
    
