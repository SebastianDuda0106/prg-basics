def power(x,n):
    if x==1:
        return 1
    if n==1:
        return x
    if x>1 and n>1:
        return x*power(x,n-1)

print(power(5,3))