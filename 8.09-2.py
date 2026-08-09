a=input()
b=input()

if a[0]==b[-1] and a[-1]==b[0] and len(a)==len(b):
    print('고리 단어쌍입니다.')
else:
    print('고리 단어쌍이 아닙니다.')
