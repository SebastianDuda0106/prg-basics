def f(text):
    char=[]
    lenght=len(text)
    for i in range(0,lenght):
        if text[i]==text[lenght-i-1]:
            #print(text[i])
            #print(text[lenght-i-1])
            continue
        else:
            return False
    return True

print(f("radar"))
print(f("12-11-21"))
print(f("book"))