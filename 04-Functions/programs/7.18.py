def f(sentence):
    word=""
    for i in range(0,len(sentence)):
        if sentence[i]==" ":
            continue
        else:
            word+=sentence[i]
    return word

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))