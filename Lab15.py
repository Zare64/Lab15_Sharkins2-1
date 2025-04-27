import matplotlib.pyplot as plt
from math import sin, pi

x_values = range(-300, 301)
x_values = [x/60 for x in x_values]
y_values = [sin(x) for x in x_values]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.set_title("Sine Wave", fontsize=24)
ax.plot(x_values, y_values)




# Set the range for each axis.
ax.axis([-5, 5, -2, 2])
plt.show()