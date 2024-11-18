import random
arr=[[random.randint(1,9) for x in range(0,2)],
     [random.randint(1,9) for x in range(0,2)],
     [random.randint(1,9) for x in range(0,2)],
     [random.randint(1,9) for x in range(0,2)]
     ]

print(arr)
for row in arr:
    for num in row:
        print(num,end=" ")
    print("")