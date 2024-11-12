arr=[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
def printar(array):
    for row in arr:
        for i in range(0,len(row)):
            print(row[i],end=" ")
        print()
    print()

printar(arr)

line=0
for row in arr:
    for i in range(0,len(row)):
        if line==i:
            row[i]=1
    line+=1

printar(arr)