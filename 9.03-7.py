'''
def max_num(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    elif c>=a and c>=b:
        print(c)
max_num(1,2,3)
max_num(-1,2,13)
max_num(5,7,7)
'''
def max_num(a,b,c):
    print(max(a,b,c))
    
max_num(1,2,3)
max_num(-1,2,13)
max_num(5,7,7)
