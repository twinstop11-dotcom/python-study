a=0
m=0
for i in range(1,51):
    sum=0
    for j in range(1,i+1):
        if i%j==0:
            sum=sum+1
    if sum>m:
        m=sum
        a=i
print(m)
print(a)

            
