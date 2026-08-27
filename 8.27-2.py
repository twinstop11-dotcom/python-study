L=[]

a=input()
while a!='-1':
    L.append(a.split(':'))
    a=input()

h=0
m=0
s=0

for i in range(len(L)):
    h=h+int(L[i][0])
    m=m+int(L[i][1])
    s=s+int(L[i][2])
if m>=60:
    h=h+(m//60)
    m=m%60
if s>=60:
    m=m+(s//60)
    s=s%60




    
print(f'{h}시 {m}분 {s}초')


   
    
    
