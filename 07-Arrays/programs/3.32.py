import random

arr=[[random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)]
     ]

arr2=[arr[-1]]+arr[1:-1]+[arr[0]]

for row in arr:
    for num in row:
        
        print(num,end=" ")
    print("")
print (arr2)
for row in arr2:
    for num in row:
        
        print(num,end=" ")
    print("")
    