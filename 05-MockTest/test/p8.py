def f(palindrom):
    fpalindrom=f"{palindrom}"
    for i in range(0,len(fpalindrom)):
        if fpalindrom[i].upper()==fpalindrom[len(fpalindrom)-i-1].upper():
            continue
        else:
            return False
    return True
if __name__ =="__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))
    print(f("Sebastian"))
    print(f("amema"))