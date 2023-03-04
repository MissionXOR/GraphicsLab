import numpy as np
import matplotlib.pyplot as plt

# Prompt user to enter center coordinates and radius of circle
x_center = int(input("Enter x-coordinate of center: "))
y_center = int(input("Enter y-coordinate of center: "))
radius = int(input("Enter radius of circle: "))

# Initialize the x and y coordinates
x = 0
y = radius
d = 1 - radius

# Create a NumPy array to store the points on the circumference of the circle
points = np.zeros((radius + 1, 2))

# Use the midpoint circle algorithm to generate the points on the circumference
while x <= y:
    points[x] = [x + x_center, y + y_center]
    points[y] = [y + x_center, x + y_center]
    points[-x] = [-x + x_center, y + y_center]
    points[-y] = [-y + x_center, x + y_center]

    x += 1
    if d < 0:
        d += 2 * x + 1
    else:
        y -= 1
        d += 2 * (x - y) + 1

# Plot the points on the circumference of the circle
plt.scatter(points[:, 0], points[:, 1])
plt.gca().set_aspect('equal')
plt.show()
