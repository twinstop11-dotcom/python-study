a=input()
b=input()
c=input()

i=max(len(a) ,len(b) ,len(c))
for j in range(0,i):
    if len(a)>j:
        print(a[j], end='')
    if len(b)>j:
        print(b[j], end='')
    if len(c)>j:
        print(c[j], end='')
    
