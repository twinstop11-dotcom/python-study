import time

n=int(input('폭팔까지 시간 설정:'))

for i in range(n,0,-1):
    print(f'{i}초 후 폭발')
    time.sleep(1)
print('퍼어엉!!')
