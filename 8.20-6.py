
print('숫자를 입력하세요.')
L=[]

a=int(input())
while a!=-1:
    L.append(a)
    a=int(input())
avg=round(sum(L)/len(L),2)
print(f'최대: {max(L)}/최소: {min(L)}/평균: {avg}')



