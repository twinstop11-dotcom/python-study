print('5개의 단어를 하나씩 입력하세요.')
L=[]

for i in range(5):
    a=input()
    L.append(a)
L.sort()
for i in range(5):
    print(L[i],end='-')

    
