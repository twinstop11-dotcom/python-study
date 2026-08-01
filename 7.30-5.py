n=int(input('몇 번째 쌍둥이소수를 찾을까요?'))
a=2
count=0
while a>0:
    a=a+1
    sum=0
    # 첫번째 값이 소수인가
    for i in range(1,a+1):
        if a%i==0:
            sum=sum+1
    #만약 소수라면
    if sum==2:
        b=a+2
        sum=0
        #두번째 값이 소수인가
        for i in range(1,b+1):
            if b%i==0:
                sum=sum+1
        #만약 둘다 소수라면
        if sum==2:
            count=count+1

    if count==n:
        print(a,a+2)
        break
        
        
            
            

