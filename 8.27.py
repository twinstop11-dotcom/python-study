L=[]
a,b=map(int,input().split())

for i in range(a):
    m=[]
    r=chr(ord('A')+i)
    for j in range(b):
        m.append(r+str(j+1))
    L.append(m)

for e in L:
    print(e)



