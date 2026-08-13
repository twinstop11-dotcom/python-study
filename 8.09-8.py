a=input()
result=''

while len(a)>3:
    result=','+a[-3:]+result
    a=a[:-3]
    
result=a+result
print(result)
    
    
    
    
    

    
