###
# Makes a copy of a text file
#

# file names
original_file = '08-FileHandling/healthy_lifestyle.txt'
target_file = '08-FileHandling/programs/copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file,'r') as file:
   content = file.read()

# write the content to the target file (copy)
with open(target_file,'w') as file:
   file.write(content)

   
with open(original_file,'r') as file:
   print(file.read())
   
with open(target_file,'r') as file:
   print(file.read())
