###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = '08-FileHandling/it_company.csv'
position_file = '08-FileHandling/programs/software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file,'r') as file:
   with open(position_file,'w') as target:
      for line in file:
         if job_title in line:
            target.write(line)