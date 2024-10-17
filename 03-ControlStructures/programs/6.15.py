code=input("Enter EAN-13 article number: ")
if len(code)==13 and code.isdigit():
    print("Article number is correct")
    if code[0:3]=="590":
        print("Article manufactured in Poland")
else:
    print("Invalid number")