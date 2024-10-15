N = 10
sum_even = 0
a=1
# Calculate the sum of even numbers
while a < N+1:
    if a % 2 == 0:
        sum_even += a
    a+=1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

#sum_even=0
#for i in range(1, N + 1):
#    if i % 2 == 0:
#        sum_even += i
#
#print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
