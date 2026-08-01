import random

r=random.randrange(1,4)

if r==1:
    computer = '가위'
if r==2:
    computer = '바위'
if r==3:
    computer = '보'

p=input('무엇을 낼까요?')
print(f'컴퓨터는 {computer}를 냈습니다.')
if p=='가위':
    if r==1:
        print('무승부!')
    if r==2:
        print('컴퓨터 승!')
    if r==3:
        print('플레이어 승!')

if p=='바위':
    if r==1:
        print('플레이어 승!')
    if r==2:
        print('무승부!')
    if r==3:
        print('컴퓨터 승!')

if p=='보':
    if r==1:
        print('컴퓨터 승!')
    if r==2:
        print('플레이어 승!')
    if r==3:
        print('무승부!')

    

          
