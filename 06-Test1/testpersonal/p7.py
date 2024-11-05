def f(number):
    #0 1 1 2 3 5 8 13
    numbefore=0
    numnow=1
    numahead=1
    if number==numnow or number==numbefore:
        return True
    while numnow<number:
        numbefore=numnow
        numnow=numahead
        numahead=numnow+numbefore
    if numnow==number:
        return True
    else:
        return False

if __name__=="__main__":
    print(f(8))
    print(f(13))
    print(f(12))
    print(f(5))
    print(f(4))