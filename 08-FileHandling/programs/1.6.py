###
# Reads from file, line by line
#
def read_from_file(name):
    with open(f'{name}', 'r') as file:#r,w,a
        content=file.read()
    return content

file_content = read_from_file('08-FileHandling/countries.txt')

file_lines = file_content.splitlines()
file_lines.sort()
for line in file_lines:
   print(line)
