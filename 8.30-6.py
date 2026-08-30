scores={'김민성':[90,89,85],
        '정찬훈':[95,92,99],
        '주혜린':[89,93,87]}

for i in scores:
    a=scores[i]
    v=round(sum(a)/len(a),1)
    print(f'{i}: 평균 {v}점')
    
