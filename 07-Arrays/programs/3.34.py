def identity_matrix(n):
    arr=[]
    count=0
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(0)
            if j==count:
                arr[i][j]=1
            else:
                arr[i][j]=0
        count+=1
    return arr

arr=identity_matrix(3)
arr2=identity_matrix(5)
arr3=identity_matrix(8)

def showarr(arr):
    for row in arr:
        for num in row:
            
            print(num,end=" ")
        print("")

print(arr)
showarr(arr)
print(arr2)
showarr(arr2)
print(arr3)
showarr(arr3)