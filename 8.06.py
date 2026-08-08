import random
sum=0

for i in range(1000):
    a = random.randrange(1,4) #문 뒤에 자동차
    b = random.randrange(1,4) #참가자 문 뽑기
    c = random.randrange(1,4)
    while c==a or c==b:
        c = random.randrange(1,4) #사회자 문 뽑기 자동차 없음

    if a!=b:
        sum=sum+1
print(sum)

    


        
        
