import random
value=int(input('Enter value:'))
arr=[ random.randint(0,20) for x in range(0,10)]
count=0
for i in arr:
    if i>value:
        count+=1
print(arr)
print(f"there are {count} elements larger than {value} in the array")