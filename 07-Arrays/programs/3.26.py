import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values
for n in range(0,360):
   x = x + [n]

# create y values
for n in x:
   y.append(math.sin(math.radians(n)))

print(x,y)
for n in range(0,360):
    plt.plot(x, y)
plt.show()