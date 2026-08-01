n=int(input())
sum=0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
           if a!=b and a!=c and b!=c:
               sum=sum+1
print(sum)
