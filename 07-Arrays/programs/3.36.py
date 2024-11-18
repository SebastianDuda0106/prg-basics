def show2darr(arr):
    if isinstance(arr,list):
        if isinstance(arr[0],list):
            for row in arr:
                for num in row:
                    print(num,end=" ")
                print("")
        else:
            print(arr)

def convert2d(arr):
    numb=[]
    if isinstance(arr,list):
        if isinstance(arr[0],list):
            for row in arr:
                for num in row:
                    numb.append(num)
    return numb

arr1=[[2,3],[1,5]]
arr2=[[5,0,3,7,5],[9,0,9,1,2]]
arr3=[[2,1],[3,5],[7,4],[2,6]]
print(convert2d(arr1))
print(convert2d(arr2))
print(convert2d(arr3))