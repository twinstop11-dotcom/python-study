'''
L=[]
sum=0

while True:
    a=input()
    if a=='끝':
        break
    L.append(a)
    sum=sum+1

for i in range(sum):
    print(L.pop(),end=' ')
    '''

L=[]

a=input()
while a!='끝':
    L.append(a)
    a=input()


for i in range(len(L)):
    print(L.pop(), end=' ')
