
def read_from_file(name):
    with open(f'{name}', 'r') as file:#r,w,a
        content=file.read()
    return content

file_name = 'it_company.csv'
file_content=read_from_file(f"08-FileHandling/{file_name}")
file_lines=file_content.splitlines()

# Position
job_title = 'Software Engineer'
counter=1
for line in file_lines:
    if job_title in line:
        print(f"{counter}.",line)
        counter+=1