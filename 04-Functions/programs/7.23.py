def f(password):
    if len(password)>=6:
        characters=[]
        for i in range(0,len(password)):
            if password[i] in characters:
                return False
            else:
                characters.append(password[i])
        return True
    return False

print(f("ax15") )
print(f("book123") )
print(f("A2water3"))
print(f("qwerty"))
print(f("") )
