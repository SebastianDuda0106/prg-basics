def f(arr):
    num=arr[0]
    if arr[0]!=arr[1]:
        if arr[0]==arr[2]:
            num=arr[0]
        elif arr[0]!=arr[2]:
            num=arr[2]
    for i in range(len(arr)):
        if arr[i]!=num:
            return i



if __name__=="__main__":
    print(f([7,5,7,7,7,7,7,7]))