def f(num):
    word="*"
    for i in range(1,num):
        word+="/*"
    return word

print(f(4))
print(f(1))