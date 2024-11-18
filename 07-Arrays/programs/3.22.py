import random

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]

arr1=[random.randint(0,25) for x in range(0,10)]
print(arr1)
print(rand_elem(arr1))