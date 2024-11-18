def arrlarg2(arr):
    counter=0
    counter2=0
    for i in arr:
        if counter<int(i):
            counter2=counter
            counter=int(i)

    return counter2

def arrdiff(arr):
    larg=0
    smal=0
    for i in arr:
        if larg<int(i):
            larg=int(i)
        if smal>int(i):
            smal=int(i)
    return (larg-smal)

def arrmed(arr):
    if len(arr)==1:
        return arr[0]
    elif len(arr)%2==0:
        return ((arr[int(len(arr)/2+1)]+arr[int(len(arr)/2)])/2)
    elif len(arr)%2==1:
        return arr[int(len(arr)/2+1)]

def arrsmallarg(arr):
    larg=0
    smal=9999
    for i in arr:
        if larg<int(i):
            larg=int(i)
        if smal>int(i):
            smal=int(i)
    arr2=[smal,larg]
    return (arr2)

def arrminstr(arr):
    arr2=""
    for i in range(0,len(arr)-1):
        arr2+=(f"{arr[i]}-")
    arr2+=(f"{arr[-1]}")
    return arr2