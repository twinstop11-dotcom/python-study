def isPrime(n):
    cnt=0

    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            cnt=cnt+1

    if cnt == 0:
        print(1)

    else:
        print(0)
isPrime(30)
