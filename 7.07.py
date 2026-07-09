a=input('캐나다, 브라질, 덴마크, 호주 중에서 나라를 선택하세요.:')
flag=0
if a=='캐나다':
    x=input('캐나다의 수도는 어디입니까? ')
    if x=='오타와':
        print('정답입니다!')
        flag=1
    else:
        print('틀렸습니다.답은 오타와입니다')
        flag=1
if a=='브라질':
    x=input('브라질의 수도는 어디입니까?')
    
    if x=='브라질리아':
        print('정답입니다!')
        flag=1
    else:
        print('틀렸습니다.답은 브라질리아입니다')
        flag=1
if a=='덴마크':
    x=input('덴마크의 수도는 어디입니까?')
    if x=='코펜하겐':
        print('정답입니다!')
        flag=1
    else:
        print('틀렸습니다.답은 코펜하겐입니다')
        flag=1
if a=='호주':
    x=input('호주의 수도는 어디입니까?')
    if x=='캔버라':
        print('정답입니다!')
        flag=1
    else:
        print('틀렸습니다.답은 캔버라입니다')
        flag=1
if flag!=1:
     print('잘못 입력하였습니다.')

