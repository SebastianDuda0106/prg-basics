def sum_natural(n):
    if n==0 or n==1:
        return n
    if n>1:
        return n+sum_natural(n-1)

print(sum_natural(10))