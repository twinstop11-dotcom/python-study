student=1
sum=0
for i in range(1,6):
    a=int(input(f'{i}번 학생이 먹은 빵의 개수를 입력하세요:'))
    if a>sum:
        sum=a
        student=i
print(f'제일 많은 빵을 먹은 사람은 {student}번 학생입니다.')
