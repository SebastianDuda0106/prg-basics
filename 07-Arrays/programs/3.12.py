import printarr
arr1=[2,3,2,5,8,1,9,8]
checkarr=[]
for i in arr1:
    if i not in checkarr:
        checkarr.append(i)
    elif i in checkarr:
        checkarr.remove(i)
print(checkarr)