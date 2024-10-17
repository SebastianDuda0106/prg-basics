prime=int(input('prime numbers to find: '))
found=0
numfound=0
num=1
print("Prime numbers: ",end=' ')
while found<prime:
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
            elif num!=3 and (num % 3) ==0:
                break
            elif num!=5 and (num % 5) ==0:
                break
            elif num!=7 and (num % 7) ==0:
                break
            else:
                if numfound!=num:
                    numfound=num
                    found+=1
                    print(num, end=' ')
                # if input number is less than
                # or equal to 1, it is not prime
    num+=1
    