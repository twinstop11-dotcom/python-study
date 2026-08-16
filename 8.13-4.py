a=input()
b=int(input())
sum=''

for i in a:
   d=ord(i)+b
   if d>ord('Z'):
       d=d-26
   sum=sum+chr(d)
    
print(sum)
