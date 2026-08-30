distance={'장태웅':353.2,
          '최치우':298.3,
          '김주환':306.5}
sum=0
winner=''

for i in distance:
    d=distance[i]
    if d>sum:
        sum=d
        winner=i

        
print(winner)
