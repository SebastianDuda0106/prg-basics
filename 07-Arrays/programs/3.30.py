arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(0,len(arr[0])):
    arr[0][i]=i+1
for i in range(0,len(arr)):
    arr[i][0]=i+1

for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        arr[i][j]=arr[0][j]*arr[i][0]


for row in arr:
    for num in row:
        print(num,end=" ")
    print("")
        