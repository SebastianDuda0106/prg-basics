def f(arr2D):
    sums=[]
    counter=0
    counter2=0
    arr2D[0][0]+arr2D[1][0]
    for column in range(len(arr2D[0])):
        for row in range(len(arr2D)):
            counter+=arr2D[row][column]
            
        if counter in sums:
            return True
        else: 
            sums.append(counter)
        counter=0


    return False


arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]
print(f([[3,4,2],[5,1,6]]))# True 
print(f([[3,4,2],[5,1,7]])) #False 
print(f([[3,4],[5,1],[4,7]]))# True 
print(f([[3,4],[5,9],[4,7]]))# False