def f(speed1,speed2):
    #km/h m/s km=1000m h=360s
    if speed2==(speed1*1000/3600):
        return True
    else:
        return False

if __name__=="__main__":
    print(f(36,10))
    print(f(72,20))
    print(f(20,20))