def f(detector):
    count=0
    for i in range(0,len(detector)):
        if detector[i]=="+":
            count+=1
        elif detector[i]=="-":
            count-=1
        if count>=3:
            return True
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++---"))