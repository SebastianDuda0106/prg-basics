def f(darr):
    rowval=0
    colval=0
    for i in range(len(darr)):
        for j in range(len(darr[i])):
            rowval+=darr[i][j]
            colval+=darr[j][i]
        print(rowval)
        print(colval)
        if colval!=rowval:
            return False
    return True


if __name__=="__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))