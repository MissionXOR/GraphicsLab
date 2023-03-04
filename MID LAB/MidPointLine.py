# Midpoint line generation Algorithm
import matplotlib.pyplot as plt
plt.title("Midpoint Line Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d  = dy - (dx/2)
    x = x1
    y = y1

    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates)
    plt.show()

if __name__=="__main__":
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    midpoint(x1, y1, x2, y2)