import random

r=random.randrange(1,7)

while True:
    p1=input('플레이어1(발사/포기):')
    if p1=='발사':
        r=r-1
        if r==0:
            print('플레이어1 사망!')
            break
        else:
            print('방아쇠를 당겼지만 발사되지 않았습니다.')
    if p1=='포기':
        print('플레이어2 승리!')
        break
    


    p2=input('플레이어2(발사/포기):')
    if p2=='발사':
        r=r-1
        if r==0:
            print('플레이어2 사망!')
            break
        else:
            print('방아쇠를 당겼지만 발사되지 않았습니다.')
    if p2=='포기':
        print('플레이어1 승리!')
        break
    
