###
# ATM (cash machine) simulator
#

import math

balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code



while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Check pin")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Change pin")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        print(f"Your current pin is: {pin}")
    elif choice == '3':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '4':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '5':
        pin=input('put in new pin: ')
        while not pin.isdigit() or len(pin) !=4:
            pin=input('put in new pin: ')
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
