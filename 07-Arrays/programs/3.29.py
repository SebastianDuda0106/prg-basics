def create_2d_arr(x,y):
    arr=[]
    for i in range(0,x):
        arr.append([])
        for j in range(0,y):
            arr[i].append(0)
    return arr

print(create_2d_arr(3,5))