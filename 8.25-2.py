L1=[90,85,99]
L2=[100,95,94]
L3=[70,82,65]
L=[L1,L2,L3]

for i in range(0,len(L)):
    if L[i][0]>=L[i][1] and L[i][0]>=L[i][2]:
        print(f'{i+1}번: 국어')
    if L[i][1]>=L[i][0] and L[i][1]>=L[i][2]:
        print(f'{i+1}번: 수학')
    if L[i][2]>=L[i][0] and L[i][2]>=L[i][1]:
        print(f'{i+1}번: 영어')
    
