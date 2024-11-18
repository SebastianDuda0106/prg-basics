arr1=[1,2,9,4]
arr2=[1,2,3,4,5,6,7,8]
count=0
isarrin=False
for i in range(0,len(arr2)):
    if count==len(arr1):
        isarrin=True
        break
    if arr1[i] in arr2:
        count+=1
    else:
        break
print(arr1)
print(arr2)
print(isarrin)