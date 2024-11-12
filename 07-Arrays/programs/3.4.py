arr=[-15, 8, -31, 47, -2, 19]
bignum=0
smalnum=0
for i in arr:
    if bignum<i:
        bignum=i
    if smalnum>i:
        smalnum=i
print("biggest:",bignum)
print("smallest:",smalnum)