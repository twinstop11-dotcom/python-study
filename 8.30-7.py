size={'짱구':[110,30],
      '뽀로로':[65,15],
      '피카츄':[50,8]}

for i in size:
    h=size[i][0]
    w=size[i][1]
    bmi=w/((h/100)**2)
    bmi=round(bmi,2)
    size[i].append(bmi)
print(size)
  
