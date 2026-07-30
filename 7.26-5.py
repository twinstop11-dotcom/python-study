for i in range(1,51):
    sum=0
    for j in range(1,i+1):
        if i%j==0:
            sum=sum+1
    if sum==2:
        print(i, end=' ')
