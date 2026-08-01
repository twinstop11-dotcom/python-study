import time

text = 'oupggjqenp'
print(f'다음 문자열을 입력하세요: {text}')
t1 = time.time()
p=input()
t2 = time.time()

if p==text:
    print(f'걸린 시간: {t2-t1}초')
else:
    print('끝')
