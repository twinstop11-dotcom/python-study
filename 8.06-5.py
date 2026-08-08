sum=0

while True:
    a=input()

    if a=='끝':
        break
    if a[-2]=='다' or a[-2]=='까':
        sum=sum+1
print(f'다나까체는 {sum}개입니다.')
