arr=[2, 6, 4, 9, 7]
def star(n):
    text=""
    for i in range(n):
        text+="*"
    return text
for i in arr:
    print(f'{i}: {star(i)}')