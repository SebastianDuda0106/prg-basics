import re
with open("08-FileHandling/files.txt","r") as file:
    content=file.read()

pattern="(\w+\..{4})"

counta = re.findall(pattern, content)
print(counta)
