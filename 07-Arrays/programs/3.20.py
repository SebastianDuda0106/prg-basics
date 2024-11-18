import random
arr1=[random.randint(-10,10) for x in range(0,6)]
print(arr1)
arreven=[]
arrodd=[]
for num in arr1:
    if num%2:
        arrodd.append(num)
    elif num%2==0:
        arreven.append(num)
arrsort=arreven+arrodd
print(arrsort)