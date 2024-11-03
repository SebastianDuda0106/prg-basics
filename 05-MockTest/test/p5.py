def f(binary_number):
    strbin=f"{binary_number}"
    for i in range(0,len(strbin)):
        if (strbin[i]!="1" and strbin[i]!="0"):
            return False
    return True

if __name__ =="__main__":
    print(f("101101"))
    print(f("1311a10100"))