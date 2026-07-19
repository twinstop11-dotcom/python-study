a,b=map(int,input('목표금액과 끼니 수를 입력하세요:').split())
print('끼니마다 사용한 금액을 입력하세요')
sum=0
i=0

while i<b:
    i=i+1
    n=int(input())
    sum=sum+n
   

print(f'한 끼 평균 금액: {sum//b}원')

if (sum//b)<a:
    print('식비 절약에 성공했습니다!')
else:
    print('식비 절약에 실패했습니다.ㅠㅠ')
