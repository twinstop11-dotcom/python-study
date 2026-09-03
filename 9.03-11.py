def common(L1,L2):
    s1=set(L1)
    s2=set(L2)
    s3=s1&s2
    for i in s3:
        print(i, end=' ')
    print()

common([1,2,3],[2,3,4])
common(['a','b','c'],['a','e','i'])
    
    
