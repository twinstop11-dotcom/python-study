print('숫자를 입력하세요.')
L=[]

a=input()
while a!='-1':
    L.append(a)
    a=input()
print(f'입력받은 숫자 개수: {len(L)}')
