scores=[['김민성',90,89,85],
        ['정창훈',95,92,99],
        ['주혜린',89,93,87]]

d={}

for i in scores:
    key=i[0]
    value=round((i[1]+i[2]+i[3])/3,1)
    d[key]=value

print(d)
