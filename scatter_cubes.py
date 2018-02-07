"""
A program which automatically calculates and plots the first 5000 cubic numbers.

Patterns in values are highlighted in color ranging from lighter colors for lower values and darker colors for higher values. 

"""
import matplotlib.pyplot as plt

x_values=list(range(1, 5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 5100, 0, 130000000000])

plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')