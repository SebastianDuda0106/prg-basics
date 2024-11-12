def f(arr1,arr2):
    if len(arr1)==len(arr2):
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return "arrays are not the same"
    else:
        return "arrays are not the same"
    return "arrays are the same"

arr1=["water","book","sky"]
arr2=["water","book","sky"]
arr3=[True,False]
arr4=[True,False,True]
arr5=[5,3,1]
arr6=[5,3,1]
arr7=[3,2,1]
arr8=[3,2]
print(f(arr1,arr2))
print(f(arr3,arr4))
print(f(arr5,arr6))
print(f(arr7,arr8))