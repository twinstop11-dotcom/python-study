a=input()

for i in a:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        print(chr(ord(i)+32),end='')
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
        print(i,end='')
        
