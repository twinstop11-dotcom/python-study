L=[]

for i in range(2,101):
    L.append(i)
print(L)
for i in range(2,51):
    for j in range(2, (100//i)+1):
        if i*j in L:
            idx = L.index(i*j)
            L[idx] = 'x'
print(L)
