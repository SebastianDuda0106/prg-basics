arr=[[-38, 19,12], [5,40,32],[-7,11,21],[29,16,-69]]
smallest=[100,0,0]
largest=[0,0,0]
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if smallest[0]>arr[i][j]:
            smallest[0]=arr[i][j]
            smallest[1]=i+1
            smallest[2]=j+1
        if largest[0]<arr[i][j]:
            largest[0]=arr[i][j]
            largest[1]=i+1
            largest[2]=j+1
for row in arr:
    for num in row:
        
        print(num,end=" ")
    print("")

print(f'the smallest value is: {smallest[0]} and is located in row {smallest[1]} in {smallest[2]} column')
print(f'the largest value is: {largest[0]} and is located in row {largest[1]} in {largest[2]} column')