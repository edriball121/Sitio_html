def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
        else:
            primo = True
    return primo

print(isPrime(13))

#for i in range(1, 20):
#    if isPrime(i + 1):
#        print(i + 1, end=" ")
#print()