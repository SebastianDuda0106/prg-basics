def f(tree_circumference):
    #2*3.14*r=tree_circumference
    r=tree_circumference/6.28
    if (r*2)>=50:
        return True
    else:
        return False

if __name__=="__main__":
    print(f(200))
    print(f(157))
    print(f(100))
    