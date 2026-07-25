while True:
    a=int(input('큰 수를 하나 입력하세요:'))
    if a<10000:
        print('5자리 이상이어야 합니다.')
        continue

    sum=0
    for i in range(2,a+1):
        if a%i==0:
            sum=sum+1
    if sum!=1:
        print('소수가 아니네요...')
    elif sum==1:
        print('소수를 찾았습니다!')
        break
