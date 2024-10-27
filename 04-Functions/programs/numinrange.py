def ninr(n,rangbegin,rangend):
    truth = n in range(rangbegin,rangend)
    if truth == True:
        truth = "yes"
    else:
        truth="no"
    print(f"Number {n} in the range <{rangbegin},{rangend}>: {truth}")