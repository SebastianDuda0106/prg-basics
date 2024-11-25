import re
text=input("input text: ")
pattern="[aąeęiouóy]"
counta = re.findall(pattern, text)
print(len(counta))