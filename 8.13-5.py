a=input()
b=int(input())
sum=''

for i in a:
    if ord(i)>=ord('a') and ord(i)<=ord('z'):
        d=ord(i)+b
        if d >ord('z'):
            d=d-26
    elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
        d=ord(i)+b
        if d >ord('Z'):
            d=d-26
    else:
        print(i,end='')
    sum=sum+chr(d)
print(sum)

