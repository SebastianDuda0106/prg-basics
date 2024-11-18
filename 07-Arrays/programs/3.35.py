def transpose_matrix(m):
    arr2=[]
    #123 147
    #456 258
    #789 369
    if isinstance(m,list):
        if isinstance(m[0],list):
            for j in range(len(m[0])):
                arr2.append([])
                for i in range(len(m)):
                    arr2[j]+=[m[i][j]]
        else:
            arr2=m[-1::-1]
    return arr2

def show2darr(arr):
    if isinstance(arr,list):
        if isinstance(arr[0],list):
            for row in arr:
                for num in row:
                    print(num,end=" ")
                print("")
        else:
            print(arr)

m=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3,4,5],[6,7,8,9,0]]
m3=[5,6,7,8]
show2darr(m)
show2darr(transpose_matrix(m))
show2darr(m2)
show2darr(transpose_matrix(m2))
show2darr(m3)
print(transpose_matrix(m3))

