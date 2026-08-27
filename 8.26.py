L=[]

for i in range(3):
    a=input().split()
    L.append(a)

for i in range(3):
    s=L[i]
    b=s[0]
    avg=(int(s[1])+int(s[2])+int(s[3]))/3
    print(f'{b}: 평균 {round(avg, 2)}점')
