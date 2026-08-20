L=[]
for i in range(5):
    a=float(input())
    L.append(a)
L.sort()
L.pop()
L.pop(0)
print(L)

