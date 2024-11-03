def f(name):
    ll=""
    acronym=f"{name[0]}"
    for i in range(1,len(name)):
        ll=name[i-1]
        if ll==" ":
            acronym+=name[i]
    return acronym

if __name__ =="__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
    print(f("Uniwersytet Ekonomiczny w Krakowie"))