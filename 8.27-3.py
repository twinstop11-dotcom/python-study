L=[]
sum=0

a=input()
while a!='끝':
    L.append(a)
    a=input()

flag=True

for i in range(len(L)-1):
    if L[i][-1]!=L[i+1][0]:
        flag=False
    if L[0][0]!=L[-1][-1]:
        flag=False





if flag==True:
    print('고리 단어묶음입니다.')
else:
    print('고리 단어묶음이 아닙니다.')
        
        

