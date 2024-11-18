import random
arr2=[]
arr=[[random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)],
     [random.randint(0,20) for  x in range(0,3)]
     ]

for i in range(0,len(arr)):
    arr2.append([])
    arr2[i]+=([arr[i][-1]]+arr[i][1:-1]+[arr[i][0]])


for row in arr:
    for num in row:
        
        print(num,end=" ")
    print("")

print(arr2)
for row in arr2:
    for num in row:
        
        print(num,end=" ")
    print("")