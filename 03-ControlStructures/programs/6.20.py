decimaln=int(input('Enter decimal number: '))
binaryn=''
binaray=[]
i=0
while decimaln>=1:
    binaray.append(f'{decimaln % 2}')
    decimaln=decimaln//2
    i+=1
while i>=1:
    binaryn+=binaray[i-1]
    i-=1
print(binaryn)