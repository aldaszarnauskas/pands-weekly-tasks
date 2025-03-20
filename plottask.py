# Import required packages
# Working with multidimensional number arrays
import numpy as np
# Plotting
from matplotlib import pyplot as plt

# Obtain numbers from a normal distribution
norm_dist = np.random.normal(5, 2, 1000)

# Define a function
def h(x):
    return x**3

# Get the x values from 0 to 10 with a step of 0.1
xs = np.arange(0, 10, 0.1)
# Get h(x)=x^3 values
ys = h(xs)


# Create the axes
fig, ax1 = plt.subplots()
# Copy the ax1
ax2 = ax1.twinx()

# Plot a histogram
ax1.hist(norm_dist, bins=25, color='skyblue', edgecolor='black')
# Plot a grid on the ax1
ax1.grid(color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.6)
# Set the limits for the ax1 axis
xlimits = (round(min(norm_dist), 0), round(max(norm_dist), 0))
ax1.set_xlim(xlimits)
# Set the x-axis labels
ax1.set_xlabel("X", fontsize=14)
# Set the y-axis labels
ax1.set_ylabel("Frequency", fontsize=14)
# Add more ticks on the x-axis
ax1.set_xticks(np.arange(xlimits[0], xlimits[1]))

# Plot a function h(x)=x^3
ax2.plot(xs, ys, lw=2, color="darkred")
# Label the function on the plot
ax2.text(7, 800, '$h(x)=x^{3}$', fontsize = 14)
# Set the limits for the y-axis
ax2.set_ylim(0,1000)
# Label the y-axis
ax2.set_ylabel('$X^{3}$', fontsize=14)
# Set the color of the right spine to black
ax2.spines['right'].set_color('black')

# Set the title of a figure
plt.title("The Histogram of Normal Distribution and the Plot of a Function h(x)=$x^{3}$", fontsize=16)
# Save the figure a .png
plt.savefig("figure.png", dpi=300, bbox_inches = 'tight')
