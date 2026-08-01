import time

p='jamcoding'
w=1
while True:
    s=input('비밀번호를 입력하세요:')
    if s==p:
        print('잠금 해제')
        break
    else:
        print(f'틀렸습니다.{w}초 기다리세요.')
        time.sleep(w)
        w=w*2
        
        
