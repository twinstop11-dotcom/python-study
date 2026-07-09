a=int(input('생년월일을 8자로 입력하세요: '))

flag=0
x= a//10000
y= (a//100)%100
z= a%100


if (x%400 ==0) or (x%100 !=0 and x%4 ==0):
    flag=1
if y >=6 and y<=8:
    flag=1
if z%10==0:
    flag=1

if flag ==1:
    print('약의 효과를 볼 수 있습니다.')
else:
    print('약의 효과를 볼 수 없습니다.')
