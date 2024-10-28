def f(n):
    word='"'
    for i in range(1,n+1):
        word+=f"{i}"
    word+='"'
    return word

print(f(11))
print(f(4))