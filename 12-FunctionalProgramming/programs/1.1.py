n1 = int(input('num1:'))
n2 = int(input('num2:'))

# define an anonymous function
def mean(x,y):
    return (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1},{n2} is {result}")