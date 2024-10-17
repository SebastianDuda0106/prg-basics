PIN=1234
tries=3
while tries>0:
    userpin=int(input('Enter the PIN code: '))
    if userpin==PIN:
        print("payment successful")
        break
    else:
        print("Incorrect...")
        tries-=1
if tries<=0:
    print("Sorry, your payment card has been blocked.")