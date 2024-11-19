
def read_from_file(name):
    with open(f'{name}', 'r') as file:#r,w,a
        content=file.read()
    return content

file_content = read_from_file('08-FileHandling/pets.txt')
file_lines = file_content.splitlines()

total = 0
for line in file_lines:
    for word in line.split():
        total += 1
print(file_content)
print('Total words:', total)