plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    encrypt=ord(char)
    # add one to the character's code
    encrypt+=1
    # replace new character code with its
    # corresponding character (use chr())
    encrypt=chr(encrypt)
    # add encrypted character to encrypted text
    encrypted_text+=encrypt

print(f'{plain_text}')
print(f'{encrypted_text}')