'''
def longer(s1,s2):
    if len(s1)>=len(s2):
        print(s1)
    else:
        print(s2)

longer('apple','kiwi')
longer('python','java')
longer('조세호','유재석')
'''

import random

def longer(s1,s2):
    a=0
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    elif len(s1)==len(s2):
        a=random.randrange(1,3)
        if a==1:
            print(s1)
        else:
            print(s2)
    
        
        
        

longer('apple','kiwi')
longer('python','java')
longer('조세호','유재석')
