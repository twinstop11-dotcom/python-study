p=input('+,-,*,/ 중에서 연산을 선택하세요.:')
flag=0
if p=='+':
    print('덧셈을 선택하였습니다.')
    
elif p=='-':
    print('뺼셈을 선택하였습니다.')
elif p=='*':
    print('곱셈을 선택하였습니다.')
elif p=='/':
    print('나눗셈을 선택하였습니다.')
else:
    print('잘못 입력하였습니다.')
    flag=1
    
if flag!=1:
    a=int(input('첫번째 수를 입력하세요.'))
    b=int(input('두번째 수를 입력하세요.'))

    if p=='+':
        print(f'{a} {p} {b} = {a + b}입니다.')
    elif p=='-':
        print(f'{a} - {b} = {a - b}입니다.')
    elif p=='*':
        print(f'{a} * {b} = {a * b}입니다.')
    else:
        print(f'{a} / {b} = {a / b}입니다.')

