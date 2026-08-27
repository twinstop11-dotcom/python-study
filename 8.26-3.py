L=[]

for i in range(5):
    m=[]
    for j in range(5):
        m.append(5*i+j)

    if i==1 or i==3:
        m.sort(reverse=True)
    L.append(m)

a,b=map(int, input().split())
print(L[a][b])
      
