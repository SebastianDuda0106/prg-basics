def isnumbin(num):
    if f"{num}".isdigit():
        for i in range(0,len(num)):
            if (int(num[i])!=0 and int(num[i])!=1):
                return False
        return True
    else:
        return False
    