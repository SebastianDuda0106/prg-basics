def f(text):
    i=1
    text2='"'
    if len(text)>0:
        text2=f'"{text[0]}'
        while i<len(text):
            text2+="-"+text[i]
            i+=1
    text2+='"'
    return text2


print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))
