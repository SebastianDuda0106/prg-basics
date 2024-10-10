swift = input('enter SWIFT code: ')
print(
f"""Bank Code: {swift[0:4]}
Country Code: {swift[4:6]}
Location Code {swift[6:8]}"""
)
if len(swift)>8:
    print(f'Branch code: {swift[8:11]}')