a='탕'
while True:
    print(f'컴퓨터:{a}')
    if a=='탕':
        a='수'
    elif a=='수':
        a='육'
    elif a=='육':
        a='탕'
    p=input('플레이어:')
    if p!=a:
        print('플레이어 패배!')
        break

    elif p==a:
        if a=='탕':
            a='수'
        elif a=='수':
            a='육'
        elif a=='육':
            a='탕'
            
        
        
    
   
