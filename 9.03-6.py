def vowel(s):
    D={'a','e','i','o','u'}
    sum=0
    for i in s:
        if i in D:
            sum=sum+1
    print(sum)
vowel("apple")
vowel("banana")          
vowel("kiwi")     
