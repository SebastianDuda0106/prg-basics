def f(array):
    smallrow=1
    smallcol=1
    smallnum=9999 #its over nine THOUSAND
    for row in range(0,len(array)):
        for column in range(0,len(array[row])):
            if smallnum>=array[row][column]:
                smallnum=array[row][column]
                smallrow=row+1
                smallcol=column+1
    if (smallrow==smallcol):
        return True
    else:
        return False
    
    
if __name__=='__main__':
    print(f([[7,8],[5,3],[9,4]]))
    print(f([[7,8,5,3],[9,4,2,6]]))
    print(f([[7,8,5,3],[9,4,2,6],[6,6,1,9]]))
