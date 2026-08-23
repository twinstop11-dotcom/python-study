a=int(input())

L=[]

for i in range(0,a):
    L.append(False)
    
for i in range(1,a+1):
    m=1
    while i*m<a:
        L[i*m]=not(L[i*m])
        m=m+1
sum=0
for i in L:
    if i==True:
        sum=sum+1
print(sum)
