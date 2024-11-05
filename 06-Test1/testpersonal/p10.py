def f(time1,time2):
    time1s=time1
    time2s=time2
    if time1[1]==":":
        time1s=f"0{time1}"
    if time2[1]==":":
        time2s=f"0{time2}"

    if "am" in time1:
        time1s=f"{time1s[0:-2]}"
    elif "pm" in time1:
        time1s=f"{int(time1s[0:2])+12}{time1s[2:-2]}"

    if "am" in time2:
        time2s=f"{time2s[0:-2]}"
    elif "pm" in time2:
        time2s=f"{(int(time2s[0:2])+12)}{time2s[2:-2]}"
    if int(time1s[0:2])>int(time2s[0:2]):
        return time2
    elif int(time2s[0:2])>int(time1s[0:2]):
        return time1
    elif int(time1s[0:2])==int(time2s[0:2]):
        if int(time1s[3:])<=int(time2s[3:]):
            return time1
        else:
            return time2

if __name__=="__main__":
    print(f("13:06","13:12"))
    print(f("1:38pm","13:31"))
    print(f("08:08","8:01am"))
    print(f("6:00pm","18:00"))
    print(f("13:06","1:06pm"))