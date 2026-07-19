a=int(input('태어난 해를 입력하세요:'))
sum=0

for i in range(a,2024):
    if (i%4==0 and i%100!=0)or(i%400==0):
        sum=sum+1
print(f'윤년은 총 {sum}번 입니다.')
