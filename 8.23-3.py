
L1=[90,85,99]
L2=[100,95,94]
L3=[70,82,65]
L=[L1,L2,L3]
'''
for student in L:
    for score in student:
        print(score, end=' ')
    print()
'''


for i in range(0,len(L)):
    for j in range(0,len(L[i])):
        print(L[i][j],end=' ')
    print()

