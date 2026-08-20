print('5개의 수를 입력하세요.')
L=[]

for i in range(5):
    a=int(input())
    L.append(a)
avg=round(sum(L)/len(L),2)
print(f'평균값: {avg}')
print('평균값보다 큰값')
for e in range(0,len(L)):
    if L[e]>avg:
        print(L[e],end=',')
