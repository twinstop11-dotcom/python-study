import random

sum=0
for i in range(0,1000000):
    x=random.random()
    y=random.random()

    if (x**2)+(y**2)<1:
        sum=sum+1

print(sum/1000000)
    
