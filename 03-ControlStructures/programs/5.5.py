total_sum = 0
number_of_numbers=0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    number_of_numbers+=1

print(f"The total sum of the numbers is: {total_sum}")
print(f"The mean of the numbers is: {total_sum/number_of_numbers}")