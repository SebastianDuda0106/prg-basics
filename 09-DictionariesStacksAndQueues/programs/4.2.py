import queue

# creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
   
    if menu == '1':
      file_name = input('Enter file name to print: ')
      files_to_print.put(file_name)
      # add new file to the end of the queue 

    elif menu=='2':
        if files_to_print.qsize()>0:# print queue not empty
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
            try:
                with open(file_to_print,'r') as file:
                    print(file)
            except:
                print('EXCEPTION!')
        else:
            print('no filo to printo')

    elif menu == '0':
        break