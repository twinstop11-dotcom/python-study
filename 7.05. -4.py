a,b=map(int,input().split())
bmi= b/((a/100)**2)
if bmi<18.5:
    print(f'당신의 bmi는 {bmi}이며,저체중입니다.')
elif bmi>=18.5 and bmi<23:
    print(f'당신의 bmi는 {bmi}이며,정상입니다.')
elif bmi>=23 and bmi<25:
    print(f'당신의 bmi는 {bmi}이며,과체중입니다.')
else:
    print(f'당신의 bmi는 {bmi}이며,비만입니다.')

   

