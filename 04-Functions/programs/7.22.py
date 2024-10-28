def f(text):
    lb=""
    letter=""
    acronym=f"{text[0]}"
    for i in range(1,len(text)):
        lb=text[i-1]
        if lb==" ":
            acronym+=text[i]
    return acronym

print(f("Internet of Things")) #returns "IoT"
print(f("For Your Information"))# returns "FYI"
print(f("Python")) #returns "P"
