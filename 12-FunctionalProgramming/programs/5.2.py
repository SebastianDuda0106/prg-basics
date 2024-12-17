from functools import reduce

# Function to add two numbers
add=lambda x,y:x+y

numbers = [2,4,6,3,7,5]

# Using reduce to sum the numbers
result = reduce(add, list(filter(lambda x:x%2==0,numbers)))
print(result)  # Output: 15
