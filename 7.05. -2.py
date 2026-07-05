a=int(input())
if a%7==0 and a%17 !=0:
    print('짱수')
elif a%17==0 and a%7 !=0:
    print('짱짱수')
elif a%119==0:
    print('짱짱짱수')
else:
    print('그냥 수')
