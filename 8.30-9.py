a,b=map(int,input().split())

s1=set()
s2=set()

for i in range(1,a+1):
    if a%i==0:
        s1.add(i)

for i in range(1,b+1):
    if b%i==0:
        s2.add(i)

s3=s1&s2
L=list(s3)
L.sort()
print(L[-1])
